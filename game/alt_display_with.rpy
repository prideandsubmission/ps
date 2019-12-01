

##################################Thunder
transform infinite_flash:
    linear 0.1 alpha 0.4
    linear 0.1 alpha 0
    repeat

transform infinite_flashfast:
    linear 0.08 alpha 0.6
    linear 0.08 alpha 0
    repeat

transform infinite_flashfastest:
    linear 0.05 alpha 0.8
    linear 0.05 alpha 0
    repeat

transform infinite_flashfastest_fast:
    linear 0.03 alpha 0.8
    linear 0.03 alpha 0
    repeat

################################## Zoom
    
transform zoomin:
    linear 0.1 zoom 2 xpos -1600 
    linear 0.1 zoom 1.98 xpos -1584 
    repeat
    
################################### opacity + zoom in
transform zoom_opa:
    linear 0.13 alpha 0.5 zoom 1.0 
    linear 0.13 alpha 0.5 zoom 1.1
    repeat
    
transform opa:
    alpha 0.5 
