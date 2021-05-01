# desktop-image-switcher

MacOS utility to change desktop background image for all desktops

## Installation

To install system-wide to `/usr/local/bin`:

```
git clone https://github.com/GabrielDougherty/desktop-image-switcher.git
cd desktop-image-switcher
sudo make install
```

Or if you want, just run `chmod +x desktop-image-switcher` and put it where ever you like.

## Uninstall

```
cd desktop-image-switcher
sudo make uninstall
```

## Usage

To set the image for all three desktops to Peak:

```
desktop-image-switcher "/System/Library/Desktop Pictures/Peak.heic" 3
```

If you don't specify a number of desktops, desktop-image-switcher will default to 5.