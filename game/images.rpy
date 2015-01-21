init -1:
    # BACKGROUNDS
    image cuttlefish = "bg/cuttlefish-logo.jpg"
    image bg stars = "bg/starscape.jpg"
    image bg earth = "bg/earth.jpg"
    image bg farm_exterior = "bg/farm-exterior.jpg"
    image bg farm_exterior flip = im.Flip("bg/farm-exterior.jpg", horizontal = True)
    image bg farm_exterior flip burned = "bg/farm-exterior-burned.jpg"
    image bg porch = "bg/farm-porch.jpg"
    image bg wedding = "bg/wedding.jpg"
    image bg farm_interior = "bg/farm-interior.jpg"
    image bg farm_interior flip = im.Flip("bg/farm-interior.jpg", horizontal = True)
    image bg fields = "bg/fields.jpg"
    image bg fields flip = im.Flip("bg/fields.jpg", horizontal = True)
    image bg colony_ship_bunk = "bg/colony-ship-bunk.jpg"
    image bg talam = "bg/talam.jpg"
    image bg talaam_space = "bg/talaam-from-space.jpg"
    image bg pond = "bg/pond.jpg"
    image bg path = "bg/path.jpg"
    image bg laundry = "bg/laundry.jpg"
    image bg library = "bg/library.jpg"
    image bg classroom = "bg/classroom.jpg"
    image bg clinic = "bg/clinic.jpg"
    image bg bedroom = "bg/bedroom.jpg"
    image bg sunset = "bg/sunset.jpg"
    image bg machine_shop = "bg/machine-shop.jpg"
    image bg workshop = "bg/workshop.jpg"
    image bg ocean = "bg/ocean.jpg"
    image bg storehouse = "bg/storehouse.jpg"
    image bg community_center = "bg/community-center.jpg"
    image bg lab = "bg/lab.jpg"
    image bg barn = "bg/barn.jpg"
    image bg mountains = "bg/mountains.jpg"
    image bg stream = "bg/stream.jpg"
    image bg hotspring = "bg/hot-spring.jpg"
    image bg tractor = "bg/tractor.jpg"
    image bg church = "bg/church.jpg" #TODO: Use another image with better license.
    image bg city_street = "bg/city-street.jpg"
    image bg bathhouse = "bg/bathhouse.jpg"
    image bg gray_silk = "bg/silk-gray.jpg"

    image cg_together = "bg/cg-1.png"
    image cg_with_baby = "bg/cg-2.png"
    image cg_earth = "bg/cg-3.png"

    image night = "bg/night.png"
    image bathhouse_overlay = "bg/bathhouse-overlay.png"
    image bedroom_covers = "bg/bedroom-overlay.png"
    image computer_pad = "bg/computer-pad.png"
    image underwater = "bg/underwater-overlay.png"
    image pond_overlay = "bg/pond-overlay.png"
    image hot_spring_overlay = "bg/hot-spring-overlay.png"

    image talaam_approach = "bg/talaam-approach.png"

    # Tutorial screenshots
    image screenshot = "bg/screenshot.jpg"
    image screenshot_left = "bg/screenshot-left.jpg"
    image screenshot_center = "bg/screenshot-center.jpg"
    image screenshot_right = "bg/screenshot-right.jpg"


    # SPRITES

    # Him
    image him normal = "sprites/him.png"
    image him angry = "sprites/him-angry.png"
    image him annoyed = "sprites/him-annoyed.png"
    image him concerned = "sprites/him-concerned.png"
    image him flirting = "sprites/him-flirt.png"
    image him happy = "sprites/him-happy.png"
    image him laughing = "sprites/him-happy.png"
    image him sad = "sprites/him-sad.png"
    image him surprised = "sprites/him-surprised.png"
    image him serious = "sprites/him-annoyed.png"
    image him sleeping = "sprites/him-sleeping.png"

    # Him nude for swimming, bath, sleeping, etc.
    image him nude = "sprites/him-nude.png"
    image him nude normal = "sprites/him-nude.png"
    image him nude angry = "sprites/him-nude-angry.png"
    image him nude annoyed = "sprites/him-nude-annoyed.png"
    image him nude concerned = "sprites/him-nude-concerned.png"
    image him nude flirting = "sprites/him-nude-flirt.png"
    image him nude happy = "sprites/him-nude-happy.png"
    image him nude sad = "sprites/him-nude-sad.png"
    image him nude surprised = "sprites/him-nude-surprised.png"
    image him nude serious = "sprites/him-nude-annoyed.png"
    image him nude sleeping = "sprites/him-nude-sleeping.png"

    # Her sprites are declared automatically in images-her.rpy
    # TODO: Use determined?

    define SMALL_IMAGE_SCALE = 0.55
    define SMALL_IMAGE_CROP = 90

    # Create the small headshot icons used on the computer screen to show each person's mood
    image her sad head = LiveCrop((5, 0, SMALL_IMAGE_CROP, SMALL_IMAGE_CROP), im.FactorScale("sprites/her/sad.png", SMALL_IMAGE_SCALE))
    image her concerned head = LiveCrop((5, 0, SMALL_IMAGE_CROP, SMALL_IMAGE_CROP), im.FactorScale("sprites/her/concerned.png", SMALL_IMAGE_SCALE))
    image her serious head = LiveCrop((5, 0, SMALL_IMAGE_CROP, SMALL_IMAGE_CROP), im.FactorScale("sprites/her/serious.png", SMALL_IMAGE_SCALE))
    image her normal head = LiveCrop((5, 0, SMALL_IMAGE_CROP, SMALL_IMAGE_CROP), im.FactorScale("sprites/her/normal.png", SMALL_IMAGE_SCALE))
    image her happy head = LiveCrop((5, 0, SMALL_IMAGE_CROP, SMALL_IMAGE_CROP), im.FactorScale("sprites/her/happy.png", SMALL_IMAGE_SCALE))

    image him concerned head = LiveCrop((5, 0, SMALL_IMAGE_CROP, SMALL_IMAGE_CROP), im.FactorScale("sprites/him-concerned.png", SMALL_IMAGE_SCALE))
    image him annoyed head = LiveCrop((5, 0, SMALL_IMAGE_CROP, SMALL_IMAGE_CROP), im.FactorScale("sprites/him-annoyed.png", SMALL_IMAGE_SCALE))
    image him normal head = LiveCrop((5, 0, SMALL_IMAGE_CROP, SMALL_IMAGE_CROP), im.FactorScale("sprites/him.png", SMALL_IMAGE_SCALE))
    image him happy head = LiveCrop((5, 0, SMALL_IMAGE_CROP, SMALL_IMAGE_CROP), im.FactorScale("sprites/him-happy.png", SMALL_IMAGE_SCALE))


    # Other Characters
    image baby girl = "sprites/baby1.png"
    image baby boy = "sprites/baby2.png"
    image baby black = "sprites/baby7.png"
    image sara = "sprites/sara.png"
    image sara normal = "sprites/sara.png"
    image sara sad = "sprites/sara-sad.png"
    image pavel = "sprites/pavel.png"
    image pavel normal = "sprites/pavel.png"
    image pavel sad = "sprites/pavel-sad.png"
    image thuc = "sprites/thuc.png"
    image thuc normal = "sprites/thuc.png"
    image thuc sad = "sprites/thuc-sad.png"
    image natalia = "sprites/natalia.png"
    image julia = "sprites/julia.png"
    image julia normal = "sprites/julia.png"
    image julia mad = "sprites/julia-mad.png"
    image brennan = "sprites/brennan.png"
    image brennan normal = "sprites/brennan.png"
    image brennan happy = "sprites/brennan-happy.png"
    image brennan mad = "sprites/brennan-mad.png"
    image lily = "sprites/lily.png"
    image lily normal = "sprites/lily.png"
    image lily upset = "sprites/lily-upset.png"
    image lily happy = "sprites/lily-happy.png"
    image naomi = "sprites/naomi.png"
    image naomi normal = "sprites/naomi.png"
    image naomi sad = "sprites/naomi-sad.png"
    image pete = "sprites/pete.png"
    image pete normal = "sprites/pete.png"
    image pete happy = "sprites/pete-happy.png"
    image helen = "sprites/helen.png"
    image helen happy = "sprites/helen-happy.png"
    image ilian = "sprites/ilian.png"
    image ilian normal = "sprites/ilian.png"
    image ilian happy = "sprites/ilian-happy.png"
    image martin = "sprites/martin.png"
    image martin normal = "sprites/martin.png"
    image martin happy = "sprites/martin-happy.png"
    image martin sad = "sprites/martin-upset.png"

    # Kids
    image van = "sprites/van.png"
    image van normal = "sprites/van.png"
    image van wince = "sprites/van-wince.png"
    image raul = "sprites/raul.png"
    image kid = "sprites/vani.png"  #TODO: add in these in more places?
    image kid normal = "sprites/vani.png"
    image kid frown = "sprites/vani-frown.png"

    # Animals
    image lettie = "sprites/horse.png"
    image lettie_head = LiveCrop((0,0,300,570), "sprites/horse.png")
    image goat = "sprites/goat.png"
    image goat_flip = im.Flip("sprites/goat.png", horizontal = True)
    image goat_small = im.FactorScale("sprites/goat.png", 0.85)
    image seastar = "sprites/seastar.png"


    # GUI
    image ctc_blink:
           "GUI/ctc.png"
           linear 0.75 alpha 1.0
           linear 0.75 alpha 0.0
           repeat 