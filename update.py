#!/usr/bin/python3
import asyncio
import io
import os
import pathlib
import ssl
import zipfile

import aiohttp


async def fetch_asset(session: aiohttp.ClientSession, release: str,
                      asset_name: str, asset_download_url: str):
    print(f"* Downloading asset {asset_name}")
    async with session.get(asset_download_url) as resp:
        zip_resp = await resp.read()
        z = zipfile.ZipFile(io.BytesIO(zip_resp))
        # Preprocess folder name, for example:
        # webfont-iosevka-17.1.0.zip -> iosevka
        folder = asset_name.strip(".zip").\
            strip(f"-{release}").strip("webfont-")
        z.extractall(f"latest/{folder}")
        print(f"  Downloaded asset {asset_name} "
              f"and extracted to latest/{folder}")


async def fetch():
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    # NOTE(kiennt26): This is a workaround with SSL handshake issue
    ssl_ctx = ssl.create_default_context()
    ssl_ctx.set_ciphers("DEFAULT")
    # trust_env -> Get proxy environment variables and use it
    # raise_for_status -> Raise an aiohttp.ClientResponseError
    # if the response status is 400 or higher.
    async with aiohttp.ClientSession(
            headers=headers,
            trust_env=True,
            connector=aiohttp.TCPConnector(ssl=ssl_ctx),
            raise_for_status=True) as session:
        # Get latest release
        latest_url = "http://api.github.com/repos/be5invis/Iosevka/releases/latest"
        async with session.get(latest_url) as resp:
            latest = await resp.json()
            # Check if the release already exists
            if os.path.exists("LATEST_RELEASE"):
                with open("LATEST_RELEASE") as f:
                    current_version = f.read()
                    if current_version == latest["tag_name"]:
                        print(f"Release {current_version} already exists,"
                              "up-to-date, skip!")
                        return

            print(f"Fetching Iosevka release {latest['tag_name']}...")

            for asset in latest["assets"]:
                # Filter webfont
                if "webfont" in asset["name"]:
                    release = latest["tag_name"].strip("v")  # number only
                    # Fetch all webfont asset
                    await fetch_asset(session, release, asset["name"],
                                      asset["browser_download_url"])

        # Update the latest release
        with open("LATEST_RELEASE", "w") as f:
            f.write(latest["tag_name"])

if __name__ == "__main__":
    print("##########################")
    print("# Get the latest release #")
    print("##########################")
    # Create directory
    pathlib.Path("latest").mkdir(parents=True, exist_ok=True)
    asyncio.run(fetch())
    print("########")
    print("# Done #")
    print("########")
