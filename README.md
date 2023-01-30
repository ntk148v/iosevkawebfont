# Iosevka webfont

The [issue](https://github.com/google/fonts/issues/559) to add [Iosevka font](https://github.com/be5invis/Iosevka) doesn't seem to be processed. Therefore, I create my own Iosevka webfont hosting using Github Page (inspired by [Pvinis](https://github.com/pvinis/iosevka-webfont)).

## How to use

- Add `<link href="https://ntk148v.github.io/iosevkawebfont/latest/<variant-name>/<variant-name>.css" rel="stylesheet" />` to your `<head>`. Change `<variant-name>` to proper variant, for example: `iosevka-curly`, `iosevka-curly-slab`...Every Iosevka webfonts are collected. For the complete list, you may want to check [latest](./latest/) folder. At this time, this is only the latest version hosted here (check the current latest version [here](./LATEST_RELEASE)).
- For example to use Iosevka curly webfonts, follow:
  - Add `<link href="https://ntk148v.github.io/iosevkawebfont/latest/iosevka-curly/iosevka-curly.css" rel="stylesheet" />` to your `<head>`.
  - Use `fontFamily: 'Iosevka Curly Web'` or `font-family: 'Iosevka Curly Web'`.
- **DEPRECATED NOTE**: For backward compatible, I keep the previous version, you still can access it with url `<link href="https://ntk148v.github.io/iosevkawebfont/latest/iosevka.css" rel="stylesheet" />`

## How to update

I use a [Python script](./update.py) to fetch all assets of the latest release. Combining with Github action, it is looking for the new release everyday and update automatically.
