# Python project design

Written in python `pygame` because this is only a map editor for bigger project and that was the fastest way to go.

This will be probably used as map creating tool while working on DOOM-like game in C.
It can add and delete nodes, considering linked list-like structure making sure lines are correct. After all it can move existing nodes, so we can create shape that we like. I probably overcoded some functionality about data structures but I dove into C lately and I loved that. So I tried to recreate some of C structures in python (EVEN IF THERE IS ABSOLUTELY NO NEED FOR THAT :) )

# TODO
- [x] Adding points
- [x] Removing points
- [x] Moving existing nodes
- [x] Correct lines
- [x] Snap points to grid based on scale and resolution (when adding and when moving)
- [ ] There is certain usecase when lines are incorrect
- [ ] Maybe multiple modes (for example. 'adding', 'removing', 'connecting') instead of different mouse clicks
- [ ] Serialization (export to binary?)
- [ ] Saving and loading

# Screens
<img src='screens/screen_1.png'></img>
