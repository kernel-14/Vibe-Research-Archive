# Figure Types — Layout Language

Each type fixes ONLY the spatial grammar. No domain content here.

## architecture
Left-to-right pipeline. Large stage cards, compact substeps, thin connectors, a visible terminal artifact, optional cross-cutting tracks.

## roadmap
Time / dependency graph. Phases as horizontal bands or stacked rows; milestones as nodes; edges for dependency or causality; clear input → output direction.

## schema
Compact card layout. Header bar, stacked field rows, tag pills, generous padding, no clutter.

## chart
Clean academic chart. Readable axes, light grid, balanced margins, legend with discrete glyphs, subtle markers.

## tracks
Two or more horizontal lanes/tracks. Labeled nodes per lane, small functional icons, clear coupling/independence between lanes.

## generic
Free-form explanatory composition with hierarchy, functional icons, tidy labels. Use when the brief does not match the above.

## Default aspect ratios

```
architecture : 16:9 wide
roadmap      : 16:9 wide or 3:2 landscape
schema       : 2:3 portrait or square
chart        : 4:3 landscape
tracks       : 16:9 wide
generic      : 3:2 landscape
```

User override always wins.
