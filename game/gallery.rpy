#################################################################
# Gallery code
# from leon on the lemmasoft forums:
# http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=22465
#
init python:
    #Galleries settings - start
    #list the CG gallery images here:
    gallery_cg_items = ["talaam_approach","cg_earth", "cg_together", "cg_with_baby"]
    
    #how many rows and columns in the gallery screens?
    gal_rows = 2
    gal_cols = 2
    #thumbnail size in pixels:
    thumbnail_x = 267
    thumbnail_y = 150
    #the setting above (267x150) will work well with 16:9 screen ratio. Make sure to adjust it, if your are using 4:3 or something else.
    #Galleries settings - end
   
    gal_cells = gal_rows * gal_cols   
    g_cg = Gallery()
    for gal_item in gallery_cg_items:
        g_cg.button(gal_item + " thumb")
        g_cg.image(gal_item)
    g_cg.transition = fade
    cg_page=0

   
init +1 python:
    #Here we create the thumbnails. We create a grayscale thumbnail image for BGs, but we use a special "locked" image for CGs to prevent spoilers.
    for gal_item in gallery_cg_items:
        renpy.image (gal_item + " thumb", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))
      
screen cg_gallery:
    tag menu
    use navigation
    frame background None xpos 0.5 ypos 0.5:
        grid gal_rows gal_cols:
            ypos 10
            $ i = 0
            $ next_cg_page = cg_page + 1           
            if next_cg_page > int(len(gallery_cg_items)/gal_cells):
                $ next_cg_page = 0
            for gal_item in gallery_cg_items:
                $ i += 1
                if i <= (cg_page+1)*gal_cells and i>cg_page*gal_cells:
                    $ from string import capwords
                    $ button_name = capwords(gal_item.replace("_", " "))
                    textbutton button_name action Replay(gal_item) xalign 0.5
                    #imagebutton idle thumb_name action Replay(gal_item)
                    #add g_cg.make_button(gal_item + " thumb", gal_item + " thumb", im.Scale("bg/gallocked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
            for j in range(i, (cg_page+1)*gal_cells): #we need this to fully fill the grid
                null
        frame:
            yalign 0.97
            vbox:
                if len(gallery_cg_items)>gal_cells:
                    textbutton _("Next Page") action [SetVariable('cg_page', next_cg_page), ShowMenu("cg_gallery")]