# Iosevka webfont

The [issue](https://github.com/google/fonts/issues/559) to add Iosevka font doesn't seem to be processed. Therefore, I create my own Iosevka webfont hosting using Github Page.

## How to use

- Add `<link href="https://pvinis.github.io/iosevka-webfont/latest/iosevka.css" rel="stylesheet" />`. At this time, this is only the latest version hosted here (check the current latest version [here](./LATEST_RELEASE)).
- Use `fontFamily: 'Iosevka Web'` or `font-family: 'Iosevka Web'`.

## How to update

I use a [simple bash script](./get-fonts.sh) to get the latest release. Combining with Github action, it is looking for the new release everyday and update automatically.
