# Style Presets

A preset is `assets/styles/<key>.yaml`. Schema:

```yaml
key: <preset-name>
palette:                        # accent set; full named colors live in shared/palettes.yaml
  primary: "#..."
  secondary: "#..."
  accent: "#..."
  neutral_bg: "#..."
  neutral_text: "#..."
font:
  label: "<font-name>"
  fallback: "<font-name>"
line:
  weight: thin|medium|bold
  arrow: thin|standard
icon: flat|outline|none
background: clean|paper|grid
motion: none                    # always none for static figures
notes: "one-line intent"
```

## Built-in presets

| Key | Use for |
| --- | --- |
| `default` | Universal fallback. Conference-safe. |
| `minimal-academic` | Camera-ready. Few accents, lots of white space. |
| `colorful-method` | Method overview / architecture. Indigo/teal/coral accents, friendly fonts. |
| `grayscale-camera-ready` | Pure B/W print. Use when journal forbids color. |

## Adding a new preset

1. Copy any existing yaml to `assets/styles/<your-key>.yaml`.
2. Edit only palette/font/line/icon/background.
3. Do NOT add domain content here. If you find yourself typing a method name, stop.
4. The renderer will pick it up automatically.
