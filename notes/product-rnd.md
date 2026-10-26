# Product-side R&D (February–April 2026): methods notes

Work done while building Kakashi, a combat-sports video analysis product, that fed the later research. Only methods
are described here: the data, product numbers and third-party footage stay private, and none of it was validated
the way the research threads were.

## Technique knowledge graph
- **What:** an ensemble of LLMs read instructional material and extracted techniques, positions and the
  transitions between them into a graph database (Neo4j), one graph per instructional system.
- **Status:** not evaluated against labels. It shaped the position and technique vocabulary used later
  ([MoveHarness ontology](https://github.com/dhruvinci/moveharness/blob/main/ontology.json)).

## Striking pipeline ("Kakashi viz")
- **What:** BBoxMaskPose (two-person pose with masks) -> Depth-Anything-V2 (monocular depth) -> SAM 3D Body (3D
  bodies), then strike detection and a strike-force estimate, on one 25-second broadcast clip (750 frames).
- **Status:** unvalidated. Strike detection reached 13-21% accuracy on that clip; the force estimates (thousands of
  newtons) have no ground truth. A later audit noted it was only ever run on that one clip. Its lessons (camera
  intrinsics, two-person separation) became [movement-research](https://github.com/dhruvinci/movement-research).

## Fast measurement, slow reasoning
- **What:** a layered design: a visual classifier, a joint-aware refinement, a temporal resolver, and a VLM that
  reasons over the measured state instead of raw pixels. Design document:
  [vlm-experiments `docs/PIPELINE_ARCHITECTURE.md`](https://github.com/dhruvinci/vlm-experiments/blob/main/docs/PIPELINE_ARCHITECTURE.md).
- **Status:** not built as designed. Its premise was tested in
  [fast-slow-vision](https://github.com/dhruvinci/fast-slow-vision) (can a small fast model describe people well
  enough?) and, for geometry, in [engage3d](https://github.com/dhruvinci/engage3d).
