from datetime import datetime , timedelta


# ============================================================
# FITNESS APP
# EXERCISE KNOWLEDGE SYSTEM
# PART 1 — CORE DATABASES
# ============================================================


# ============================================================
# 1. MUSCLE DATABASE
# ============================================================
MUSCLES = {

    # Chest Subdivisions
    "upper_chest": "Upper Chest",
    "middle_chest": "Middle Chest",
    "lower_chest": "Lower Chest",
    "pectoralis_major": "Chest",
    "pectoralis_minor": "Chest",

    # Back Subdivisions
    "lat_width": "Lats (Back Width)",
    "upper_back": "Upper Back & Mid-Back",
    "lower_back": "Lower Back Strength",
    "latissimus_dorsi": "Lats",
    "trapezius": "Upper Back (Traps)",
    "rhomboids": "Mid-Back",
    "teres_major": "Upper Lats",
    "erector_spinae": "Lower Back",

    # Shoulders
    "front_shoulder": "Front Shoulder",
    "side_shoulder": "Side Shoulder",
    "rear_shoulder": "Rear Shoulder",
    "anterior_deltoid": "Front Shoulder",
    "lateral_deltoid": "Side Shoulder",
    "posterior_deltoid": "Rear Shoulder",

    # Biceps / Arms
    "biceps_outer": "Biceps (Outer Peak)",
    "biceps_inner": "Biceps (Inner Thickness)",
    "biceps_brachii": "Biceps",
    "brachialis": "Outer Bicep / Forearm Tie-in",
    "brachioradialis": "Top Forearm",

    # Triceps
    "triceps_long": "Triceps (Back of Arm)",
    "triceps_outer": "Triceps (Outer Head)",
    "triceps_inner": "Triceps (Inner Head)",
    "triceps_brachii": "Triceps",

    # Forearms
    "forearm_flexors": "Inner Forearm",
    "forearm_extensors": "Outer Forearm",

    # Quadriceps
    "quads": "Thighs (Front Quads)",
    "rectus_femoris": "Thighs (Front Quads)",
    "vastus_lateralis": "Thighs (Outer Quads)",
    "vastus_medialis": "Thighs (Tear-drop Quads)",
    "vastus_intermedius": "Thighs (Inner Quads)",

    # Hamstrings
    "hamstrings": "Hamstrings (Back of Thigh)",
    "biceps_femoris": "Hamstrings (Outer)",
    "semitendinosus": "Hamstrings (Inner)",
    "semimembranosus": "Hamstrings (Deep Inner)",

    # Glutes
    "glutes_main": "Glutes (Main Butt Muscle)",
    "glutes_side": "Side Glutes",
    "gluteus_maximus": "Glutes (Main Butt Muscle)",
    "gluteus_medius": "Side Glutes",
    "gluteus_minimus": "Deep Side Glutes",

    # Calves
    "calves_upper": "Upper Calves",
    "calves_lower": "Lower Calves",
    "gastrocnemius": "Upper Calves",
    "soleus": "Lower Calves",

    # Core
    "abs_front": "Abs (Front Pack)",
    "abs_sides": "Obliques (Side Abs)",
    "rectus_abdominis": "Front Abs",
    "external_oblique": "Side Abs",
    "internal_oblique": "Deep Side Abs",
    "transversus_abdominis": "Core Shield"
}

# ============================================================
# USER-FACING PLAN ANALYSIS TRANSLATIONS (Independent Map)
# ============================================================

SIMPLE_MUSCLE_NAMES = {
    # Chest subdivisions
    "upper_chest": "Upper Chest",
    "middle_chest": "Middle Chest",
    "lower_chest": "Lower Chest",

    # Triceps heads
    "triceps_long": "Triceps (Back of Arm)",
    "triceps_outer": "Triceps (Outer Head)",
    "triceps_inner": "Triceps (Inner Head)",

    # Biceps heads
    "biceps_outer": "Biceps (Outer Peak)",
    "biceps_inner": "Biceps (Inner Thickness)",
    
    # Back subdivisions
    "lat_width": "Lats (Back Width)",
    "upper_back": "Upper Back & Mid-Back",
    "lower_back": "Lower Back Strength",
    
    # Lower Body subdivisions
    "quads": "Thighs (Front Quads)",
    "hamstrings": "Hamstrings (Back of Thigh)",
    "glutes_main": "Glutes (Main Butt Muscle)",
    "glutes_side": "Side Glutes",
    "calves_upper": "Upper Calves",
    "calves_lower": "Lower Calves",
    
    # Core subdivisions
    "abs_front": "Abs (Front Pack)",
    "abs_sides": "Obliques (Side Abs)"
}


# ============================================================
# 2. BODY PARTS
# ============================================================

BODY_PARTS = [

    "Chest",
    "Back",
    "Shoulders",
    "Biceps",
    "Triceps",
    "Forearms",
    "Quadriceps",
    "Hamstrings",
    "Glutes",
    "Calves",
    "Core"

]


# ============================================================
# 3. MOVEMENT PATTERNS
# ============================================================

MOVEMENTS = {

    "horizontal_push": "Horizontal Push",
    "vertical_push": "Vertical Push",

    "horizontal_pull": "Horizontal Pull",
    "vertical_pull": "Vertical Pull",

    "elbow_flexion": "Elbow Flexion",
    "elbow_extension": "Elbow Extension",

    "shoulder_abduction": "Shoulder Abduction",
    "shoulder_extension": "Shoulder Extension",

    "horizontal_adduction": "Horizontal Adduction",
    "horizontal_abduction": "Horizontal Abduction",

    "knee_extension": "Knee Extension",
    "knee_flexion": "Knee Flexion",

    "hip_extension": "Hip Extension",
    "hip_abduction": "Hip Abduction",

    "hip_hinge": "Hip Hinge",

    "ankle_plantarflexion": "Ankle Plantarflexion",

    "trunk_flexion": "Trunk Flexion",

    "anti_extension": "Anti-Extension",
    "anti_lateral_flexion": "Anti-Lateral Flexion",

    "loaded_carry": "Loaded Carry"
}


# ============================================================
# 4. EQUIPMENT
# ============================================================

EQUIPMENT = [

    "Barbell",
    "Dumbbells",
    "Cable",
    "Machine",
    "Bodyweight",
    "EZ-Bar",
    "Kettlebell",
    "Smith Machine",
    "Resistance Band",
    "Landmine",
    "Ab Wheel"

]


# ============================================================
# 5. DAYS OF THE WEEK
# ============================================================

DAYS = [

    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"

]


# ============================================================
# 6. CHECK THAT PART 1 WORKED
# =========================================================

# ============================================================
# FITNESS APP
# PART 2 — EXERCISE KNOWLEDGE DATABASE
# ============================================================


EXERCISES = {

    # ========================================================
    # CHEST
    # ========================================================

    "barbell_bench_press": {
        "id": "barbell_bench_press",
        "name": "Barbell Bench Press",
        "body_parts": ["Chest"],
        "type": "Compound",
        "equipment": "Barbell",
        "movement": "Horizontal Push",
        "primary_muscles": ["pectoralis_major"],
        "secondary_muscles": ["anterior_deltoid", "triceps_brachii"],
        "aliases": ["bench press", "barbell press", "flat bench press"],
        "biometric_distribution": {
            "middle_chest": 0.65,
            "lower_chest": 0.20,
            "upper_chest": 0.15
        }
    },

    "dumbbell_bench_press": {
        "id": "dumbbell_bench_press",
        "name": "Dumbbell Bench Press",
        "body_parts": ["Chest"],
        "type": "Compound",
        "equipment": "Dumbbells",
        "movement": "Horizontal Push",
        "primary_muscles": ["pectoralis_major"],
        "secondary_muscles": ["anterior_deltoid", "triceps_brachii"],
        "aliases": ["db bench press", "dumbbell press", "flat dumbbell press"],
        "biometric_distribution": {
            "middle_chest": 0.60,
            "lower_chest": 0.25,
            "upper_chest": 0.15
        }
    },

    "incline_barbell_bench_press": {
        "id": "incline_barbell_bench_press",
        "name": "Incline Barbell Bench Press",
        "body_parts": ["Chest"],
        "type": "Compound",
        "equipment": "Barbell",
        "movement": "Horizontal Push",
        "primary_muscles": ["pectoralis_major"],
        "secondary_muscles": ["anterior_deltoid", "triceps_brachii"],
        "aliases": ["incline bench press", "incline barbell press"],
        "biometric_distribution": {
            "upper_chest": 0.70,
            "middle_chest": 0.25,
            "lower_chest": 0.05
        }
    },

    "incline_dumbbell_press": {
        "id": "incline_dumbbell_press",
        "name": "Incline Dumbbell Press",
        "body_parts": ["Chest"],
        "type": "Compound",
        "equipment": "Dumbbells",
        "movement": "Horizontal Push",
        "primary_muscles": ["pectoralis_major"],
        "secondary_muscles": ["anterior_deltoid", "triceps_brachii"],
        "aliases": ["incline db press", "incline dumbbell bench"],
        "biometric_distribution": {
            "upper_chest": 0.65,
            "middle_chest": 0.30,
            "lower_chest": 0.05
        }
    },

    "decline_barbell_bench_press": {
        "id": "decline_barbell_bench_press",
        "name": "Decline Barbell Bench Press",
        "body_parts": ["Chest"],
        "type": "Compound",
        "equipment": "Barbell",
        "movement": "Horizontal Push",
        "primary_muscles": ["pectoralis_major"],
        "secondary_muscles": ["triceps_brachii", "anterior_deltoid"],
        "aliases": ["decline bench press", "decline press"],
        "biometric_distribution": {
            "lower_chest": 0.65,
            "middle_chest": 0.30,
            "upper_chest": 0.05
        }
    },

    "machine_chest_press": {
        "id": "machine_chest_press",
        "name": "Machine Chest Press",
        "body_parts": ["Chest"],
        "type": "Compound",
        "equipment": "Machine",
        "movement": "Horizontal Push",
        "primary_muscles": ["pectoralis_major"],
        "secondary_muscles": ["anterior_deltoid", "triceps_brachii"],
        "aliases": ["chest press machine", "machine press"],
        "biometric_distribution": {
            "middle_chest": 0.65,
            "lower_chest": 0.20,
            "upper_chest": 0.15
        }
    },

    "cable_chest_press": {
        "id": "cable_chest_press",
        "name": "Cable Chest Press",
        "body_parts": ["Chest"],
        "type": "Compound",
        "equipment": "Cable",
        "movement": "Horizontal Push",
        "primary_muscles": ["pectoralis_major"],
        "secondary_muscles": ["anterior_deltoid", "triceps_brachii"],
        "aliases": ["cable press", "standing cable chest press"],
        "biometric_distribution": {
            "middle_chest": 0.50,
            "lower_chest": 0.35,
            "upper_chest": 0.15
        }
    },

    "pec_deck": {
        "id": "pec_deck",
        "name": "Pec Deck",
        "body_parts": ["Chest"],
        "type": "Isolation",
        "equipment": "Machine",
        "movement": "Horizontal Adduction",
        "primary_muscles": ["pectoralis_major"],
        "secondary_muscles": [],
        "aliases": ["pec fly", "machine chest fly", "chest fly machine"],
        "biometric_distribution": {
            "middle_chest": 0.70,
            "lower_chest": 0.20,
            "upper_chest": 0.10
        }
    },

    "cable_chest_fly": {
        "id": "cable_chest_fly",
        "name": "Cable Chest Fly",
        "body_parts": ["Chest"],
        "type": "Isolation",
        "equipment": "Cable",
        "movement": "Horizontal Adduction",
        "primary_muscles": ["pectoralis_major"],
        "secondary_muscles": [],
        "aliases": ["cable fly", "standing cable fly", "chest cable fly"],
        "biometric_distribution": {
            "lower_chest": 0.50,
            "middle_chest": 0.40,
            "upper_chest": 0.10
        }
    },

    "dumbbell_chest_fly": {
        "id": "dumbbell_chest_fly",
        "name": "Dumbbell Chest Fly",
        "body_parts": ["Chest"],
        "type": "Isolation",
        "equipment": "Dumbbells",
        "movement": "Horizontal Adduction",
        "primary_muscles": ["pectoralis_major"],
        "secondary_muscles": [],
        "aliases": ["db fly", "dumbbell fly"],
        "biometric_distribution": {
            "middle_chest": 0.60,
            "lower_chest": 0.25,
            "upper_chest": 0.15
        }
    },

    "push_up": {
        "id": "push_up",
        "name": "Push-Up",
        "body_parts": ["Chest"],
        "type": "Compound",
        "equipment": "Bodyweight",
        "movement": "Horizontal Push",
        "primary_muscles": ["pectoralis_major"],
        "secondary_muscles": ["anterior_deltoid", "triceps_brachii"],
        "aliases": ["pushup", "press up"],
        "biometric_distribution": {
            "middle_chest": 0.55,
            "lower_chest": 0.30,
            "upper_chest": 0.15
        }
    },

    "weighted_push_up": {
        "id": "weighted_push_up",
        "name": "Weighted Push-Up",
        "body_parts": ["Chest"],
        "type": "Compound",
        "equipment": "Bodyweight",
        "movement": "Horizontal Push",
        "primary_muscles": ["pectoralis_major"],
        "secondary_muscles": ["anterior_deltoid", "triceps_brachii"],
        "aliases": ["weighted pushup"],
        "biometric_distribution": {
            "middle_chest": 0.55,
            "lower_chest": 0.30,
            "upper_chest": 0.15
        }
    },

    # ========================================================
    # BACK
    # ========================================================

    "pull_up": {
        "id": "pull_up",
        "name": "Pull-Up",
        "body_parts": ["Back"],
        "type": "Compound",
        "equipment": "Bodyweight",
        "movement": "Vertical Pull",
        "primary_muscles": ["latissimus_dorsi"],
        "secondary_muscles": ["biceps_brachii", "brachialis"],
        "aliases": ["pullup", "wide grip pullup"],
        "biometric_distribution": {
            "lat_width": 0.75,
            "upper_back": 0.25
        }
    },

    "chin_up": {
        "id": "chin_up",
        "name": "Chin-Up",
        "body_parts": ["Back", "Biceps"],
        "type": "Compound",
        "equipment": "Bodyweight",
        "movement": "Vertical Pull",
        "primary_muscles": ["latissimus_dorsi", "biceps_brachii"],
        "secondary_muscles": ["brachialis", "brachioradialis"],
        "aliases": ["chinup", "underhand pullup"],
        "biometric_distribution": {
            "lat_width": 0.60,
            "biceps_inner": 0.40
        }
    },

    "lat_pulldown": {
        "id": "lat_pulldown",
        "name": "Lat Pulldown",
        "body_parts": ["Back"],
        "type": "Compound",
        "equipment": "Cable",
        "movement": "Vertical Pull",
        "primary_muscles": ["latissimus_dorsi"],
        "secondary_muscles": ["biceps_brachii", "brachialis"],
        "aliases": ["pulldown", "lat pull down"],
        "biometric_distribution": {
            "lat_width": 0.80,
            "upper_back": 0.20
        }
    },

    "barbell_row": {
        "id": "barbell_row",
        "name": "Barbell Row",
        "body_parts": ["Back"],
        "type": "Compound",
        "equipment": "Barbell",
        "movement": "Horizontal Pull",
        "primary_muscles": ["latissimus_dorsi", "trapezius", "rhomboids"],
        "secondary_muscles": ["posterior_deltoid", "biceps_brachii", "erector_spinae"],
        "aliases": ["bent over row", "barbell bent over row"],
        "biometric_distribution": {
            "upper_back": 0.55,
            "lat_width": 0.30,
            "lower_back": 0.15
        }
    },

    "dumbbell_row": {
        "id": "dumbbell_row",
        "name": "Dumbbell Row",
        "body_parts": ["Back"],
        "type": "Compound",
        "equipment": "Dumbbells",
        "movement": "Horizontal Pull",
        "primary_muscles": ["latissimus_dorsi", "rhomboids"],
        "secondary_muscles": ["posterior_deltoid", "biceps_brachii"],
        "aliases": ["db row", "one arm dumbbell row"],
        "biometric_distribution": {
            "lat_width": 0.55,
            "upper_back": 0.45
        }
    },

    "seated_cable_row": {
        "id": "seated_cable_row",
        "name": "Seated Cable Row",
        "body_parts": ["Back"],
        "type": "Compound",
        "equipment": "Cable",
        "movement": "Horizontal Pull",
        "primary_muscles": ["latissimus_dorsi", "rhomboids"],
"secondary_muscles": ["trapezius", "posterior_deltoid", "biceps_brachii"],"aliases": ["cable row", "seated row"],"biometric_distribution": {"upper_back": 0.60,"lat_width": 0.40}},


    "chest_supported_row": {"id": "chest_supported_row","name": "Chest-Supported Row","body_parts": ["Back"],"type": "Compound","equipment": "Machine","movement": "Horizontal Pull","primary_muscles": ["rhomboids", "trapezius", "latissimus_dorsi"],"secondary_muscles": ["posterior_deltoid", "biceps_brachii"],"aliases": ["chest supported machine row"],"biometric_distribution": {"upper_back": 0.70,"lat_width": 0.30}},"straight_arm_pulldown": {"id": "straight_arm_pulldown","name": "Straight-Arm Pulldown","body_parts": ["Back"],"type": "Isolation","equipment": "Cable","movement": "Shoulder Extension","primary_muscles": ["latissimus_dorsi"],"secondary_muscles": ["teres_major"],"aliases": ["straight arm pulldown", "cable pullover"],"biometric_distribution": {"lat_width": 0.90,"upper_back": 0.10}},"barbell_shrug": {"id": "barbell_shrug","name": "Barbell Shrug","body_parts": ["Back"],"type": "Isolation","equipment": "Barbell","movement": "Loaded Carry","primary_muscles": ["trapezius"],"secondary_muscles": [],"aliases": ["shrugs", "barbell shrugs"],"biometric_distribution": {"upper_back": 1.00  # Completely targets upper traps/neck line
    }},


    # ========================================================
    # SHOULDERS
    # ========================================================

"barbell_overhead_press": {"id": "barbell_overhead_press","name": "Barbell Overhead Press","body_parts": ["Shoulders"],"type": "Compound","equipment": "Barbell","movement": "Vertical Push","primary_muscles": ["anterior_deltoid", "lateral_deltoid"],"secondary_muscles": ["triceps_brachii"],"aliases": ["ohp", "military press", "barbell shoulder press"],"biometric_distribution": {"front_shoulder": 0.70,"side_shoulder": 0.30}},"dumbbell_shoulder_press": {"id": "dumbbell_shoulder_press","name": "Dumbbell Shoulder Press","body_parts": ["Shoulders"],"type": "Compound","equipment": "Dumbbells","movement": "Vertical Push","primary_muscles": ["anterior_deltoid", "lateral_deltoid"],"secondary_muscles": ["triceps_brachii"],"aliases": ["db shoulder press", "dumbbell overhead press"],"biometric_distribution": {"front_shoulder": 0.65,"side_shoulder": 0.35}},"machine_shoulder_press": {"id": "machine_shoulder_press","name": "Machine Shoulder Press","body_parts": ["Shoulders"],"type": "Compound","equipment": "Machine","movement": "Vertical Push","primary_muscles": ["anterior_deltoid", "lateral_deltoid"],"secondary_muscles": ["triceps_brachii"],"aliases": ["shoulder press machine"],"biometric_distribution": {"front_shoulder": 0.75,"side_shoulder": 0.25}},"dumbbell_lateral_raise": {"id": "dumbbell_lateral_raise","name": "Dumbbell Lateral Raise","body_parts": ["Shoulders"],"type": "Isolation","equipment": "Dumbbells","movement": "Shoulder Abduction","primary_muscles": ["lateral_deltoid"],"secondary_muscles": [],"aliases": ["lateral raise", "side raise", "db lateral raise"],"biometric_distribution": {"side_shoulder": 1.00}},"cable_lateral_raise": {"id": "cable_lateral_raise","name": "Cable Lateral Raise","body_parts": ["Shoulders"],"type": "Isolation","equipment": "Cable","movement": "Shoulder Abduction","primary_muscles": ["lateral_deltoid"],"secondary_muscles": [],"aliases": ["cable side raise"],"biometric_distribution": {"side_shoulder": 1.00}},"reverse_pec_deck": {"id": "reverse_pec_deck","name": "Reverse Pec Deck","body_parts": ["Shoulders", "Back"],"type": "Isolation","equipment": "Machine","movement": "Horizontal Abduction","primary_muscles": ["posterior_deltoid"],"secondary_muscles": ["trapezius", "rhomboids"],"aliases": ["rear delt machine", "reverse fly machine"],"biometric_distribution": {"rear_shoulder": 0.70,"upper_back": 0.30}},"dumbbell_rear_delt_fly": {"id": "dumbbell_rear_delt_fly","name": "Dumbbell Rear Delt Fly","body_parts": ["Shoulders"],"type": "Isolation","equipment": "Dumbbells","movement": "Horizontal Abduction","primary_muscles": ["posterior_deltoid"],"secondary_muscles": ["rhomboids", "trapezius"],"aliases": ["rear delt fly", "reverse dumbbell fly"],"biometric_distribution": {"rear_shoulder": 0.75,"upper_back": 0.25}},


    # ========================================================
    # BICEPS
    # ========================================================
"barbell_curl": {"id": "barbell_curl","name": "Barbell Curl","body_parts": ["Biceps"],"type": "Isolation","equipment": "Barbell","movement": "Elbow Flexion","primary_muscles": ["biceps_brachii"],"secondary_muscles": ["brachialis", "brachioradialis"],"aliases": ["barbell biceps curl"],"biometric_distribution": {"biceps_inner": 0.50,"biceps_outer": 0.50}},"ez_bar_curl": {"id": "ez_bar_curl","name": "EZ-Bar Curl","body_parts": ["Biceps"],"type": "Isolation","equipment": "EZ-Bar","movement": "Elbow Flexion","primary_muscles": ["biceps_brachii"],"secondary_muscles": ["brachialis", "brachioradialis"],"aliases": ["ez curl", "ez bar biceps curl"],"biometric_distribution": {"biceps_outer": 0.60,"biceps_inner": 0.40}},"dumbbell_curl": {"id": "dumbbell_curl","name": "Dumbbell Curl","body_parts": ["Biceps"],"type": "Isolation","equipment": "Dumbbells","movement": "Elbow Flexion","primary_muscles": ["biceps_brachii"],"secondary_muscles": ["brachialis", "brachioradialis"],"aliases": ["db curl", "dumbbell bicep curl"],"biometric_distribution": {"biceps_inner": 0.50,"biceps_outer": 0.50}},"hammer_curl": {"id": "hammer_curl","name": "Hammer Curl","body_parts": ["Biceps"],"type": "Isolation","equipment": "Dumbbells","movement": "Elbow Flexion","primary_muscles": ["brachialis", "brachioradialis"],"secondary_muscles": ["biceps_brachii"],"aliases": ["db hammer curl", "neutral grip curl"],"biometric_distribution": {"biceps_outer": 0.80,  # Shifting high strain onto the brachialis/outer ridge line
"biceps_inner": 0.20}},"incline_dumbbell_curl": {"id": "incline_dumbbell_curl","name": "Incline Dumbbell Curl","body_parts": ["Biceps"],"type": "Isolation","equipment": "Dumbbells","movement": "Elbow Flexion","primary_muscles": ["biceps_brachii"],"secondary_muscles": ["brachialis"],"aliases": ["incline db curl"],"biometric_distribution": {"biceps_outer": 0.75,  # Maximises long head stretch peak
"biceps_inner": 0.25}},"preacher_curl": {"id": "preacher_curl","name": "Preacher Curl","body_parts": ["Biceps"],"type": "Isolation","equipment": "Machine","movement": "Elbow Flexion","primary_muscles": ["biceps_brachii"],"secondary_muscles": ["brachialis"],"aliases": ["preacher bicep curl"],"biometric_distribution": {"biceps_inner": 0.75,  # Short head absolute thickness biomechanics focus
"biceps_outer": 0.25}},"cable_curl": {"id": "cable_curl","name": "Cable Curl","body_parts": ["Biceps"],"type": "Isolation","equipment": "Cable","movement": "Elbow Flexion","primary_muscles": ["biceps_brachii"],"secondary_muscles": ["brachialis", "brachioradialis"],"aliases": ["standing cable curl"],"biometric_distribution": {"biceps_inner": 0.50,"biceps_outer": 0.50}},



    # ========================================================
    # TRICEPS
    # ========================================================
"triceps_pushdown": {"id": "triceps_pushdown","name": "Triceps Pushdown","body_parts": ["Triceps"],"type": "Isolation","equipment": "Cable","movement": "Elbow Extension","primary_muscles": ["triceps_brachii"],"secondary_muscles": [],"aliases": ["tricep pushdown", "cable pushdown", "rope pushdown"],"biometric_distribution": {"triceps_outer": 0.50,"triceps_inner": 0.30,"triceps_long": 0.20}},"overhead_cable_triceps_extension": {"id": "overhead_cable_triceps_extension","name": "Overhead Cable Triceps Extension","body_parts": ["Triceps"],"type": "Isolation","equipment": "Cable","movement": "Elbow Extension","primary_muscles": ["triceps_brachii"],"secondary_muscles": [],"aliases": ["overhead cable extension"],"biometric_distribution": {"triceps_long": 0.70,"triceps_outer": 0.15,"triceps_inner": 0.15}},"skull_crusher": {"id": "skull_crusher","name": "Skull Crusher","body_parts": ["Triceps"],"type": "Isolation","equipment": "EZ-Bar","movement": "Elbow Extension","primary_muscles": ["triceps_brachii"],"secondary_muscles": [],"aliases": ["lying triceps extension", "ez bar skull crusher"],"biometric_distribution": {"triceps_long": 0.55,"triceps_outer": 0.25,"triceps_inner": 0.20}},"close_grip_bench_press": {"id": "close_grip_bench_press","name": "Close-Grip Bench Press","body_parts": ["Triceps", "Chest"],"type": "compound","equipment": "Barbell","movement": "Horizontal Push","primary_muscles": ["triceps_brachii"],"secondary_muscles": ["pectoralis_major", "anterior_deltoid"],"aliases": ["close grip bench", "close grip press"],"biometric_distribution": {"triceps_outer": 0.40,"triceps_inner": 0.40,"middle_chest": 0.20}},

#=================================
           #QUADRICEPS
#=====≠===============================
"back_squat": {"id": "back_squat","name": "Back Squat","body_parts": ["Quadriceps", "Glutes"],"type": "Compound","equipment": "Barbell","movement": "Knee + Hip Extension","primary_muscles": ["rectus_femoris", "vastus_lateralis", "vastus_medialis", "vastus_intermedius"],"secondary_muscles": ["gluteus_maximus", "erector_spinae"],"aliases": ["barbell squat", "squat"],"biometric_distribution": {"quads": 0.60,"glutes_main": 0.40}},"front_squat": {"id": "front_squat","name": "Front Squat","body_parts": ["Quadriceps", "Glutes"],"type": "Compound","equipment": "Barbell","movement": "Knee + Hip Extension","primary_muscles": ["rectus_femoris", "vastus_lateralis", "vastus_medialis", "vastus_intermedius"],"secondary_muscles": ["gluteus_maximus"],"aliases": ["barbell front_squat"],"biometric_distribution": {"quads": 0.75,"glutes_main": 0.25}},"leg_press": {"id": "leg_press","name": "Leg Press","body_parts": ["Quadriceps", "Glutes"],"type": "Compound","equipment": "Machine","movement": "Knee + Hip Extension","primary_muscles": ["rectus_femoris", "vastus_lateralis", "vastus_medialis", "vastus_intermedius"],"secondary_muscles": ["gluteus_maximus"],"aliases": ["leg press machine"],"biometric_distribution": {"quads": 0.70,"glutes_main": 0.30}},"hack_squat": {"id": "hack_squat","name": "Hack Squat","body_parts": ["Quadriceps", "Glutes"],"type": "Compound","equipment": "Machine","movement": "Knee + Hip Extension","primary_muscles": ["rectus_femoris", "vastus_lateralis", "vastus_medialis", "vastus_intermedius"],"secondary_muscles": ["gluteus_maximus"],"aliases": ["hack squat machine"],"biometric_distribution": {"quads": 0.80,"glutes_main": 0.20}},"leg_extension": {"id": "leg_extension","name": "Leg Extension","body_parts": ["Quadriceps"],"type": "Isolation","equipment": "Machine","movement": "Knee Extension","primary_muscles": ["rectus_femoris", "vastus_lateralis", "vastus_medialis", "vastus_intermedius"],"secondary_muscles": [],"aliases": ["quad extension"],"biometric_distribution": {"quads": 1.00}},"bulgarian_split_squat": {"id": "bulgarian_split_squat","name": "Bulgarian Split Squat","body_parts": ["Quadriceps", "Glutes"],"type": "Compound","equipment": "Dumbbells","movement": "Knee + Hip Extension","primary_muscles": ["rectus_femoris", "vastus_lateralis", "vastus_medialis", "vastus_intermedius"],"secondary_muscles": ["gluteus_maximus"],"aliases": ["rear foot elevated split squat", "split squat"],"biometric_distribution": {"glutes_main": 0.50,"quads": 0.50}},
#====================================
           #HAMSTRING
#====================================
"romanian_deadlift": {"id": "romanian_deadlift","name": "Romanian Deadlift","body_parts": ["Hamstrings", "Glutes"],"type": "Compound","equipment": "Barbell","movement": "Hip Hinge","primary_muscles": ["biceps_femoris", "semitendinosus", "semimembranosus"],"secondary_muscles": ["gluteus_maximus", "erector_spinae"],"aliases": ["rdl", "barbell rdl"],"biometric_distribution": {"hamstrings": 0.60,"glutes_main": 0.30,"lower_back": 0.10}},"dumbbell_romanian_deadlift": {"id": "dumbbell_romanian_deadlift","name": "Dumbbell Romanian Deadlift","body_parts": ["Hamstrings", "Glutes"],"type": "Compound","equipment": "Dumbbells","movement": "Hip Hinge","primary_muscles": ["biceps_femoris", "semitendinosus", "semimembranosus"],"secondary_muscles": ["gluteus_maximus"],"aliases": ["db rdl", "dumbbell rdl"],"biometric_distribution": {"hamstrings": 0.65,"glutes_main": 0.35}},"lying_leg_curl": {"id": "lying_leg_curl","name": "Lying Leg Curl","body_parts": ["Hamstrings"],"type": "Isolation","equipment": "Machine","movement": "Knee Flexion","primary_muscles": ["biceps_femoris", "semitendinosus", "semimembranosus"],"secondary_muscles": [],"aliases": ["leg curl", "lying hamstring curl"],"biometric_distribution": {"hamstrings": 1.00}},"seated_leg_curl": {"id": "seated_leg_curl","name": "Seated Leg Curl","body_parts": ["Hamstrings"],"type": "Isolation","equipment": "Machine","movement": "Knee Flexion","primary_muscles": ["biceps_femoris", "semitendinosus", "semimembranosus"],"secondary_muscles": [],"aliases": ["seated hamstring curl"],"biometric_distribution": {"hamstrings": 1.00}},
#=====================
#     GLUTES  
#======================
"barbell_hip_thrust": {"id": "barbell_hip_thrust","name": "Barbell Hip Thrust","body_parts": ["Glutes"],"type": "Compound","equipment": "Barbell","movement": "Hip Extension","primary_muscles": ["gluteus_maximus"],"secondary_muscles": ["biceps_femoris", "semitendinosus", "semimembranosus"],"aliases": ["hip thrust"],"biometric_distribution": {"glutes_main": 0.80,"hamstrings": 0.20}},"glute_bridge": {"id": "glute_bridge","name": "Glute Bridge","body_parts": ["Glutes"],"type": "Compound","equipment": "Bodyweight","movement": "Hip Extension","primary_muscles": ["gluteus_maximus"],"secondary_muscles": [],"aliases": ["bodyweight glute bridge"],"biometric_distribution": {"glutes_main": 1.00}},"cable_kickback": {"id": "cable_kickback","name": "Cable Glute Kickback","body_parts": ["Glutes"],"type": "Isolation","equipment": "Cable","movement": "Hip Extension","primary_muscles": ["gluteus_maximus"],"secondary_muscles": [],"aliases": ["cable kickback", "glute kickback"],"biometric_distribution": {"glutes_main": 1.00}},"hip_abduction_machine": {"id": "hip_abduction_machine","name": "Hip Abduction Machine","body_parts": ["Glutes"],"type": "Isolation","equipment": "Machine","movement": "Hip Abduction","primary_muscles": ["gluteus_medius", "gluteus_minimus"],"secondary_muscles": [],"aliases": ["abduction machine", "hip abduction"],"biometric_distribution": {"glutes_side": 1.00}},
#===========
#CALVES
#====≠======
"standing_calf_raise": {"id": "standing_calf_raise","name": "Standing Calf Raise","body_parts": ["Calves"],"type": "Isolation","equipment": "Machine","movement": "Ankle Plantarflexion","primary_muscles": ["gastrocnemius"],"secondary_muscles": ["soleus"],"aliases": ["calf raise"],"biometric_distribution": {"calves_upper": 0.75,"calves_lower": 0.25}},"seated_calf_raise": {"id": "seated_calf_raise","name": "Seated Calf Raise","body_parts": ["Calves"],"type": "Isolation","equipment": "Machine","movement": "Ankle Plantarflexion","primary_muscles": ["soleus"],"secondary_muscles": ["gastrocnemius"],"aliases": ["seated calf raise"],"biometric_distribution": {"calves_lower": 0.80,"calves_upper": 0.20}},
#====≠==========
#     CORE
#===============
"cable_crunch": {"id": "cable_crunch","name": "Cable Crunch","body_parts": ["Core"],"type": "Isolation","equipment": "Cable","movement": "Trunk Flexion","primary_muscles": ["rectus_abdominis"],"secondary_muscles": ["external_oblique", "internal_oblique"],"aliases": ["kneeling cable crunch"],"biometric_distribution": {"abs_front": 0.80,"abs_sides": 0.20}},"crunch": {"id": "crunch","name": "Crunch","body_parts": ["Core"],"type": "Isolation","equipment": "Bodyweight","movement": "Trunk Flexion","primary_muscles": ["rectus_abdominis"],"secondary_muscles": [],"aliases": ["ab crunch"],"biometric_distribution": {"abs_front": 1.00}},"hanging_leg_raise": {"id": "hanging_leg_raise","name": "Hanging Leg Raise","body_parts": ["Core"],"type": "Compound","equipment": "Bodyweight","movement": "Hip Flexion","primary_muscles": ["rectus_abdominis"],"secondary_muscles": [],"aliases": ["hanging leg raises"],"biometric_distribution": {"abs_front": 1.00  # High lower abs emphasis
}},"ab_wheel_rollout": {"id": "ab_wheel_rollout","name": "Ab Wheel Rollout","body_parts": ["Core"],"type": "Compound","equipment": "Ab Wheel","movement": "Anti-Extension","primary_muscles": ["rectus_abdominis", "transversus_abdominis"],"secondary_muscles": ["external_oblique", "internal_oblique"],"aliases": ["ab rollout", "wheel rollout"],"biometric_distribution": {"abs_front": 0.70,"abs_sides": 0.30}},"plank": {"id": "plank","name": "Plank","body_parts": ["Core"],"type": "Isometric","equipment": "Bodyweight","movement": "Anti-Extension","primary_muscles": ["transversus_abdominis", "rectus_abdominis"],"secondary_muscles": ["external_oblique", "internal_oblique"],"aliases": ["front plank"],"biometric_distribution": {"abs_front": 0.60,"abs_sides": 0.40}}}

# ============================================================
# FITNESS APP
# PART 3 — EXERCISE SEARCH & SELECTION
# ============================================================


# ============================================================
# 1. SEARCH EXERCISES
# ============================================================

def search_exercises(search_text):

    search_text = search_text.lower().strip()

    results = []

    for exercise_id, exercise in EXERCISES.items():

        name = exercise["name"].lower()

        aliases = [
            alias.lower()
            for alias in exercise["aliases"]
        ]

        body_parts = [
            part.lower()
            for part in exercise["body_parts"]
        ]

        # Search name
        if search_text in name:
            results.append(exercise_id)
            continue

        # Search aliases
        if any(search_text in alias for alias in aliases):
            results.append(exercise_id)
            continue

        # Search body part
        if any(search_text in part for part in body_parts):
            results.append(exercise_id)
            continue

    return results


# ============================================================
# 2. DISPLAY EXERCISE DETAILS
# ============================================================

def show_exercise(exercise_id):

    exercise = EXERCISES[exercise_id]

    print("\n==========================================")
    print(exercise["name"])
    print("==========================================")

    print(
        "Body Part:",
        ", ".join(exercise["body_parts"])
    )

    print(
        "Type:",
        exercise["type"]
    )

    print(
        "Equipment:",
        exercise["equipment"]
    )

    print(
        "Movement:",
        exercise["movement"]
    )

    print("\nPrimary Muscles:")

    for muscle in exercise["primary_muscles"]:

        if muscle in MUSCLES:
            print(
                " -",
                MUSCLES[muscle]
            )

    print("\nSecondary Muscles:")

    if exercise["secondary_muscles"]:

        for muscle in exercise["secondary_muscles"]:

            if muscle in MUSCLES:
                print(
                    " -",
                    MUSCLES[muscle]
                )

    else:

        print(" - None listed")


# ============================================================
# 3. SEARCH + SELECT ONE EXERCISE
# ============================================================

def select_exercise():

    search_text = input(
        "\nSearch exercise: "
    )

    results = search_exercises(search_text)

    if not results:

        print(
            "\nNo exercises found."
        )

        return None


    print("\nMatching Exercises:")

    for number, exercise_id in enumerate(
        results,
        start=1
    ):

        print(
            f"{number}. {EXERCISES[exercise_id]['name']}"
        )


    while True:

        choice = input(
            "\nSelect exercise number: "
        )

        try:

            choice = int(choice)

            if 1 <= choice <= len(results):

                selected_id = results[choice - 1]

                show_exercise(selected_id)

                return selected_id

            else:

                print(
                    "Please enter a valid number."
                )

        except ValueError:

            print(
                "Please enter a number."
            )
    # ============================================================
# FITNESS APP
# PART 4 — 7-DAY WORKOUT PLAN BUILDER
# ============================================================


# ============================================================
# 1. WORKOUT PLAN STORAGE
# ============================================================

WORKOUT_PLAN = {

    day: {
        "body_parts": [],
        "exercises": []
    }

    for day in DAYS
}


# ============================================================
# 2. SELECT BODY PARTS
# ============================================================

def select_body_parts():

    print("\n==========================================")
    print("SELECT BODY PARTS")
    print("==========================================")

    for number, body_part in enumerate(
        BODY_PARTS,
        start=1
    ):

        print(
            f"{number}. {body_part}"
        )


    print(
        "\nEnter numbers separated by commas."
    )

    print(
        "Example: 1,4"
    )


    while True:

        selection = input(
            "\nYour selection: "
        ).strip()


        try:

            numbers = [
                int(number.strip())
                for number in selection.split(",")
            ]


            selected_parts = []


            for number in numbers:

                if 1 <= number <= len(BODY_PARTS):

                    body_part = BODY_PARTS[number - 1]

                    if body_part not in selected_parts:

                        selected_parts.append(
                            body_part
                        )

                else:

                    print(
                        f"Invalid number: {number}"
                    )

                    selected_parts = []

                    break


            if selected_parts:

                return selected_parts


        except ValueError:

            print(
                "Please enter numbers only."
            )


# ============================================================
# 3. ADD EXERCISE TO DAY
# ============================================================

def add_exercise_to_day(day):

    print("\n==========================================")
    print(f"ADD EXERCISE — {day}")
    print("==========================================")


    selected_exercise = select_exercise()


    if selected_exercise is None:

        return False


    # --------------------------------------------------------
    # SELECTED EXERCISE IS ALREADY THE EXERCISE DICTIONARY
    # --------------------------------------------------------

    exercise = selected_exercise


    # --------------------------------------------------------
    # GET EXERCISE ID
    # --------------------------------------------------------

    selected_id = exercise.get(
        "id",
        exercise.get("exercise_id")
    )


    # --------------------------------------------------------
    # CHECK WHETHER EXERCISE MATCHES SELECTED BODY PART
    # --------------------------------------------------------

    selected_body_parts = (
        WORKOUT_PLAN[day]["body_parts"]
    )


    matching_parts = [

        part

        for part in exercise["body_parts"]

        if part in selected_body_parts

    ]


    if not matching_parts:

        print("\n------------------------------------------")
        print("WARNING:")

        print(
            f"{exercise['name']} is not directly "
            f"associated with the selected body parts."
        )

        print("------------------------------------------")


        continue_anyway = input(
            "Add it anyway? (yes/no): "
        ).lower().strip()


        if continue_anyway != "yes":

            print(
                "\nExercise not added."
            )

            return False


    # --------------------------------------------------------
    # ENTER PLANNED SETS
    # --------------------------------------------------------

    while True:

        try:

            sets = int(
                input(
                    "\nNumber of sets: "
                )
            )


            if sets > 0:

                break


            print(
                "Sets must be greater than 0."
            )


        except ValueError:

            print(
                "Please enter a whole number."
            )


    # --------------------------------------------------------
    # ENTER REPS
    # --------------------------------------------------------

    while True:

        try:

            reps = int(
                input(
                    "Target reps per set: "
                )
            )


            if reps >= 0:

                break


            print(
                "Reps cannot be negative."
            )


        except ValueError:

            print(
                "Please enter a whole number."
            )


    # --------------------------------------------------------
    # ENTER STARTING / PLANNED WEIGHT
    # --------------------------------------------------------

    while True:

        try:

            weight = float(
                input(
                    "Starting weight (0 if beginner): "
                )
            )


            if weight >= 0:

                break


            print(
                "Weight cannot be negative."
            )


        except ValueError:

            print(
                "Please enter a valid number."
            )


    # --------------------------------------------------------
    # SAVE EXERCISE
    # --------------------------------------------------------

    exercise_data = {

        "exercise_id": selected_id,

        "exercise_name": exercise["name"],

        "sets": sets,

        "reps": reps,

        "weight": weight

    }


    WORKOUT_PLAN[day]["exercises"].append(
        exercise_data
    )


    print("\n==========================================")

    print(
        f"{exercise['name']} added to {day}."
    )

    print(
        f"Sets: {sets}"
    )

    print(
        f"Reps: {reps}"
    )

    print(
        f"Weight: {weight}"
    )

    print("==========================================")


    return True


# ============================================================
# 4. SHOW DAY PLAN
# ============================================================

def show_day_plan(day):

    plan = WORKOUT_PLAN[day]


    print("\n")
    print("==========================================")
    print(f"{day.upper()} WORKOUT PLAN")
    print("==========================================")


    if not plan["body_parts"]:

        print("Body Parts: None")

    else:

        print(
            "Body Parts:",
            ", ".join(plan["body_parts"])
        )


    print("\nExercises:")


    if not plan["exercises"]:

        print("No exercises added.")

        return


    for number, exercise in enumerate(
        plan["exercises"],
        start=1
    ):

        print(
            f"\n{number}. {exercise['exercise_name']}"
        )

        print(
            f"   Sets: {exercise['sets']}"
        )

        print(
            f"   Reps: {exercise['reps']}"
        )

        print(
            f"   Weight: {exercise['weight']}"
        )

    print("\n==========================================")
# ============================================================
# 5. BUILD ONE DAY
# ============================================================

def build_day(day):

    print("\n")
    print("##########################################")
    print(f"BUILDING WORKOUT — {day.upper()}")
    print("##########################################")


    # --------------------------------------------------------
    # SELECT BODY PARTS
    # --------------------------------------------------------

    body_parts = select_body_parts()


    WORKOUT_PLAN[day]["body_parts"] = body_parts


    print("\nSelected body parts:")

    for part in body_parts:

        print(
            " -",
            part
        )


    # --------------------------------------------------------
    # ADD EXERCISES
    # --------------------------------------------------------

    while True:

        add_exercise_to_day(day)


        another = input(
            "\nAdd another exercise? (yes/no): "
        ).lower().strip()


        if another != "yes":

            break


    # --------------------------------------------------------
    # SHOW COMPLETED DAY
    # --------------------------------------------------------

    show_day_plan(day)
    
    save_day_plan(day)


# ============================================================
# 6. SELECT DAY
# ============================================================

def select_day():

    print("\n==========================================")
    print("SELECT WORKOUT DAY")
    print("==========================================")


    for number, day in enumerate(
        DAYS,
        start=1
    ):

        print(
            f"{number}. {day}"
        )


    print("8. Back")


    while True:

        try:

            choice = int(
                input(
                    "\nChoose day number: "
                )
            )


            # ----------------------------------------------
            # BACK
            # ----------------------------------------------

            if choice == 8:

                return None


            # ----------------------------------------------
            # SELECT DAY
            # ----------------------------------------------

            if 1 <= choice <= len(DAYS):

                return DAYS[choice - 1]


            print(
                "Please select a valid option."
            )


        except ValueError:

            print(
                "Please enter a number."
            )
#==================================
#ANALYSE PLANNED WORKOUT ROUTINE
#===≠==============================
def analyze_planned_workout_routine():
    # --- GLOBAL SYSTEM MAPS & THRESHOLDS ---
    MEV = 4.0                 # Minimum Effective Volume per week
    MRV = 20.0                # Maximum Recoverable Volume threshold
    SESSION_MAX_SETS = 6.0    # Junk volume ceiling per muscle per day
    MAX_SESSION_DURATION_SETS = 22 # Pillar 9: Upper limit for set quality collapse
    muscle_groups_data = {
        "Chest": ["upper_chest", "middle_chest", "lower_chest"],
        "Back": ["lat_width", "upper_back", "lower_back"],
        "Shoulders": ["front_shoulder", "side_shoulder", "rear_shoulder"],
        "Arms": ["biceps_outer", "biceps_inner", "triceps_long", "triceps_outer", "triceps_inner"],
        "Legs": ["quads", "hamstrings", "glutes_main", "glutes_side", "calves_upper", "calves_lower"],
        "Core": ["abs_front", "abs_sides"],
    }
    # Custom advice triggers for completely ignored body structures
    ignored_group_advice = {
        "Chest": "🔴 No chest exercises found! If you want a complete, balanced physique, add pressing variants or flyes.",
        "Back": "🔴 No back exercises found! Ignoring the back causes terrible posture and leaves your pull muscles underdeveloped.",
        "Shoulders": "🔴 No shoulder exercises found! A complete upper body requires side raises and pressing variants to build strength.",
        "Arms": "🔴 No arm exercises found! Consider adding direct bicep curls and tricep pushdowns to stimulate upper body mass.",
        "Legs": "🔴 No leg exercises found! Skipping quads, hamstrings, and calves limits overall structural growth and metabolism.",
        "Core": "🔴 No core exercises found! If you want torso stability and a strong midsection, add front ab work or side obliques.",
    }

    # Trackers for Multi-Session Scoring
    weekly_subdivision_volume = {}  
    muscle_frequency = {}           
    push_pull_balance = {"push": 0, "pull": 0}
    quad_hip_balance = {"quad_dominant": 0, "hip_dominant": 0}
    
    # Pillar 10: Track exact movement patterns utilized per day to catch redundancy
    daily_movement_redundancy = {} 
    
    session_warnings = []
    has_exercises = False

    # Mapping sub-keys back to their simple parent groups for broad data aggregations
    broad_group_mapping = {
        "upper_chest": "Chest", "middle_chest": "Chest", "lower_chest": "Chest",
        "triceps_long": "Triceps", "triceps_outer": "Triceps", "triceps_inner": "Triceps",
        "biceps_outer": "Biceps", "biceps_inner": "Biceps",
        "lat_width": "Back", "upper_back": "Back", "lower_back": "Back",
        "front_shoulder": "Shoulders", "side_shoulder": "Shoulders", "rear_shoulder": "Shoulders",
        "quads": "Legs (Quads)", "hamstrings": "Legs (Hamstrings)", 
        "glutes_main": "Legs (Glutes)", "glutes_side": "Legs (Glutes)",
        "calves_upper": "Legs (Calves)", "calves_lower": "Legs (Calves)",
        "abs_front": "Core", "abs_sides": "Core"
    }

    # Initialize master calculation storage maps
    weekly_subdivision_volume = {k: 0.0 for bucket in muscle_groups_data.values() for k in bucket}
    muscle_frequency = {group: 0 for group in muscle_groups_data}
    push_pull_balance = {"push": 0.0, "pull": 0.0}
    quad_hip_balance = {"quad_dominant": 0.0, "hip_dominant": 0.0}
    daily_movement_redundancy = {day: {} for day in DAYS}
    session_warnings = []
    has_exercises = False

    # 1. RUN COMPILATION LOOPS OVER THE ENTIRE WORKOUT_PLAN WEEK
    for day in DAYS:
        day_plan = WORKOUT_PLAN.get(day, {})
        planned_exercises = day_plan.get("exercises", [])
        if not planned_exercises:
            continue

        has_exercises = True
        
        muscles_tracked_today = set()
        total_session_sets = 0
        seen_isolation = False

        for item in planned_exercises:
            ex_id = item["exercise_id"]
            sets = item["sets"]
            reps = item["reps"]
            total_session_sets += sets

            db_ex = EXERCISES.get(ex_id, {})
            ex_type = db_ex.get("type", "Compound").lower()
            movement_pattern = db_ex.get("movement", "").lower()
            ex_name = db_ex.get("name", "Unknown Exercise")

            # Pillar 6: Sequence Audit
            if ex_type == "isolation":
                seen_isolation = True
            elif ex_type == "compound" and seen_isolation:
                session_warnings.append(
                    f"⚠️  {day} Order: '{ex_name}' (Compound) is scheduled after an isolation exercise.\n"
                    f"     Tip: Heavy multi-joint movements require fresh energy and should be done first."
                )

            # Pillar 7: Custom 6-10 Target Rep Range Logic
            if reps > 0 and (reps < 6 or reps > 10):
                session_warnings.append(
                    f"⚠️  {day} Reps: '{ex_name}' is set to {reps} reps.\n"
                    f"     Tip: Muscle fibers grow best when targeted between a 6-10 rep range near failure.\n"
                    f"          If it takes more than 10 reps to reach failure, consider increasing the weight.\n"
                    f"          If you cannot do 6 clean reps, consider reducing the weight."
                )

            # Pillar 10: Biomechanical Redundancy Check
            if movement_pattern:
                daily_movement_redundancy[day][movement_pattern] = daily_movement_redundancy[day].get(movement_pattern, 0) + 1
                if daily_movement_redundancy[day][movement_pattern] > 2:
                    session_warnings.append(
                        f"⚠️  {day} Redundancy: Multiple exercises use the exact same '{movement_pattern.replace('_', ' ').title()}' pattern.\n"
                        f"     Tip: Avoid stacking identical motion lines (e.g. flat bench press + flat machine press) in one day."
                    )

            # Pillar 5: Pulling / Pressing Ratios
            if "push" in movement_pattern:
                push_pull_balance["push"] += sets
            elif "pull" in movement_pattern:
                push_pull_balance["pull"] += sets

            if "extension" in movement_pattern or "squat" in movement_pattern:
                quad_hip_balance["quad_dominant"] += sets
            elif "hinge" in movement_pattern or "curl" in movement_pattern:
                quad_hip_balance["hip_dominant"] += sets

            # Accumulate fine volume fractions
            distribution = db_ex.get("biometric_distribution", {})
            for head_key, factor in distribution.items():
                if head_key in weekly_subdivision_volume:
                    effective_vol = sets * factor
                    weekly_subdivision_volume[head_key] += effective_vol

                    # Find parent muscle bucket to calculate frequency mapping parameters
                    for group_name, sub_heads in muscle_groups_data.items():
                        if head_key in sub_heads:
                            muscles_tracked_today.add(group_name)

        # Update global muscle frequency arrays
        for group in muscles_tracked_today:
            muscle_frequency[group] = muscle_frequency.get(group, 0) + 1

        # Pillar 9: Volume Cap Realism
        if total_session_sets > MAX_SESSION_DURATION_SETS:
            session_warnings.append(
                f"🚨 {day} Overload: Session features {total_session_sets} total sets.\n"
                f"     Warning: Beyond ~22 hard sets, exhaustion sets in and your execution quality completely collapses."
            )

    if not has_exercises:
        print("\nYour weekly plan is completely empty! Add exercises first to run the analysis.")
        return

    # 2. RENDER THE INTERACTIVE SMART ANALYSER NAVIGATION HUB
    while True:
        print("\n" + "#" * 42)
        print("#         🧠 SMART ROUTINE HUB          #")
        print("#" * 42)
        print("1. 🎯 Target Growth & Subdivision Balance")
        print("2. 📅 Frequency & Recovery Audit")
        print("3. ⚖️ Joint Health & Structural Balance")
        print("4. 🔍 Missing Angle Analysis")
        print("5. 🚨 Routine Structure Flags")
        print("6. ↩️ Exit Analyzer")

        hub_choice = input("\nSelect analysis module: ").strip()

        if hub_choice == "6":
            print("\nReturning to Plan Builder...")
            break

        # ====================================================
        # MODULE 1: TARGET GROWTH & SUBDIVISION SELECTOR
        # ====================================================
        elif hub_choice == "1":
            while True:
                print("\n==========================================")
                print("TARGET GROWTH: SELECT MUSCLE GROUP")
                print("==========================================")
                muscle_keys = list(muscle_groups_data.keys())
                for i, group in enumerate(muscle_keys, start=1):
                    print(f"{i}. {group}")
                print("7. ↩️ Back to Hub")

                sub_choice = input("\nChoose muscle to inspect: ").strip()
                if sub_choice == "7":
                    break

                try:
                    selected_group = muscle_keys[int(sub_choice) - 1]
                    print(f"\n--- {selected_group.upper()} GROWTH REPORT ---")

                    # Check if the muscle group is completely unassigned
                    if muscle_frequency.get(selected_group, 0) == 0:
                        print(ignored_group_advice.get(selected_group, f"🔴 No volume mapped to {selected_group}."))
                        continue

                    # Otherwise, iterate over the fine-grained subdivision metrics
                    for head_key in muscle_groups_data[selected_group]:
                        volume = weekly_subdivision_volume[head_key]
                        clean_name = MUSCLES.get(head_key, head_key.replace("_", " ").title())

                        if volume == 0:
                            status = "🔴 MISSED completely (0 Sets planned)"
                        elif volume < MEV:
                            status = f" 🟡 TOO LOW ({volume:.1f} sets | Maintenance level, won't grow fast)"
                        elif volume > MRV:
                            status = f"💥 OVERTRAINING ZONE ({volume:.1f} sets | Dangerously high volume)"
                        else:
                            status = f"✅ PERFECT GROWTH ZONE ({volume:.1f} sets)"
                        print(f" - {clean_name:<28}: {status}")

                except (ValueError, IndexError):
                    print("\nInvalid selection. Choose a number between 1 and 7.")

        # ====================================================
        # MODULE 2: FREQUENCY & RECOVERY ENGINE (WITH IGNORED HIGHLIGHTS)
        # ====================================================
        elif hub_choice == "2":
            print("\n==========================================")
            print("📅 FREQUENCY & RECOVERY CHECK")
            print("==========================================")

            # Print metrics for active muscle structures
            for group, frequency in muscle_frequency.items():
                if frequency > 0:
                    if frequency == 1:
                        print(
                            f" - {group:<15}: 🟡 Hit 1x per week. Research shows "
                            f"splitting your volume across 2 separate days triggers faster growth."
                        )
                    else:
                        print(
                            f" - {group:<15}: ✅ Hit {frequency}x per week. "
                            f"Optimal protein synthesis timing."
                        )

            # Identify and clearly point out completely ignored tracking categories
            print("\n--- 🚫 Missed Training Categories ---")
            ignored_found = False
            for group in muscle_groups_data:
                if muscle_frequency.get(group, 0) == 0:
                    print(
                        f" - {group:<15}: 🔴 IGNORED (0 times in the week. "
                        f"Your body parts will fall out of proportion!)"
                    )
                    ignored_found = True
            if not ignored_found:
                print(" ✅ Great job! Every major muscle category is scheduled at least once this week.")

        # ====================================================
        # MODULE 3: DETAILED JOINT HEALTH STRUCTURAL BALANCE CARD
        # ====================================================
        elif hub_choice == "3":
            print("\n==========================================")
            print("⚖️ JOINT HEALTH & MOVEMENT RATIOS")
            print("==========================================")
            push = push_pull_balance["push"]
            pull = push_pull_balance["pull"]
            quads = quad_hip_balance["quad_dominant"]
            hips = quad_hip_balance["hip_dominant"]

            print(f" 🔲 Upper Body : Pushing Volume = {push:.1f} sets | Pulling Volume = {pull:.1f} sets")
            print(f" 🔲 Lower Body : Quad Focus = {quads:.1f} sets | Hamstring Focus = {hips:.1f} sets")
            print("-" * 42)
            print(" 🧭 HOW TO USE THIS DATA TO GROW AND PREVENT INJURIES:")

            # Upper body structural coaching rule cards
            if push > (pull * 1.5) and pull > 0:
                print("\n🚨 UPPER BODY IMBALANCE DETECTED:")
                print("  Your plan heavily over-indexes on pressing movements (Bench, Shoulder Press).")
                print("  Why this matters: This pulls your shoulders forward, compressing your joints and causing shoulder tears.")
                print("  👉 ACTION PLAN: Add more Pulling work (Rows, Lat Pulldowns) until your Pull volume matches your Push volume.")
            elif push == 0 and pull == 0:
                print("\n Upper Body: No active upper body data calculated yet.")
            else:
                print(
                    "\n✅ UPPER BODY ALIGNMENT: Your push-to-pull layout is highly balanced. "
                    "This preserves smooth rotational mobility and opens up space for maximum muscle growth."
                )

            # Lower body structural coaching rule cards
            if quads > (hips * 2.0) and hips > 0:
                print("\n🚨 LOWER BODY IMBALANCE DETECTED:")
                print("  Your plan is highly knee-dominant, loading quads while ignoring your hamstrings/glutes.")
                print("  Why this matters: This causes knee friction, patellar tendonitis, and limits your overall leg mass potential.")
                print("  👉 ACTION PLAN: Add Romanian Deadlifts, Leg Curls, or Hip Thrusts to balance out your front-to-back muscle tissue.")
            elif quads == 0 and hips == 0:
                print("\n Lower Body: No active lower body data calculated yet.")
            else:
                print(
                    "\n✅ LOWER BODY ALIGNMENT: Your quad-to-hip load setup looks solid. "
                    "This balances knee flexion with hip drive, protecting your joints while building thicker legs."
                )

        # ====================================================
        # MODULE 4: MISSING ANGLE SCANNER (UNCHANGED BY REQUEST)
        # ====================================================
        elif hub_choice == "4":
            print("\n==========================================")
            print("🔍 MISSING ANGLE ANALYSIS")
            print("==========================================")
            missing_gaps = False

            if (weekly_subdivision_volume.get("upper_chest", 0) < 1.0
                    and weekly_subdivision_volume.get("middle_chest", 0) >= 2.0):
                print(" 🔍 Chest: Missing Upper Chest focus. Try replacing a flat bench with Incline Dumbbell Presses.")
                missing_gaps = True

            if (weekly_subdivision_volume.get("lat_width", 0) > 0
                    and weekly_subdivision_volume.get("upper_back", 0) == 0):
                print(" 🔍 Back: Routine lacks horizontal rows. Add Rows to build middle back density.")
                missing_gaps = True

            if (weekly_subdivision_volume.get("triceps_long", 0) < 1.0
                    and weekly_subdivision_volume.get("triceps_outer", 0) >= 2.0):
                print(" 🔍 Triceps: Skipping overhead extension work. Add an overhead tricep stretch movement.")
                missing_gaps = True

            if not missing_gaps:
                print(" ✅ Angle Variation: Superb layout! All target angles are covered perfectly.")

        # ====================================================
        # MODULE 5: ROUTINE FLAGS & RECODE ADJUSTMENT INSTRUCTIONS
        # ====================================================
        elif hub_choice == "5":
            print("\n==========================================")
            print("🚨 ROUTINE STRUCTURE FLAGS")
            print("==========================================")
            if session_warnings:
                for warning in session_warnings:
                    print(warning)
            else:
                print(" ✅ Structure Look Perfect: Your exercise selections and sequencing pass all core efficiency tests.")

            # Render multi-week periodization card check at the bottom
            print("\n--- ⏳ Periodization Strategy ---")
            period_check = input(
                " Is this routine plan meant to be run continuously for more than 6 weeks? (yes/no): "
            ).lower().strip()
            if period_check == "yes":
                print("\n 💡 Coach Tip: To avoid hitting plateaus, make sure to plan a 'Deload Week'")
                print("   every 6-8 weeks where you reduce total planned sets by half for recovery.")

        else:
            print("\nInvalid choice. Select an option from 1 to 6.")

        input("\nPress Enter to return to Analysis Hub Menu...")

# FITNESS APP
# PART 5 — EDIT & MANAGE WORKOUT PLAN
# ============================================================


# ============================================================
# 1. EDIT EXERCISE DETAILS
# ============================================================

def edit_exercise(day):

    exercises = WORKOUT_PLAN[day]["exercises"]

    if not exercises:

        print("\nNo exercises available to edit.")

        return


    print("\n==========================================")
    print(f"EDIT EXERCISE — {day}")
    print("==========================================")


    for number, exercise in enumerate(
        exercises,
        start=1
    ):

        print(
            f"{number}. {exercise['exercise_name']} "
            f"({exercise['sets']} sets × "
            f"{exercise['reps']} reps @ "
            f"{exercise['weight']})"
        )


    while True:

        try:

            choice = int(
                input(
                    "\nSelect exercise number: "
                )
            )


            if 1 <= choice <= len(exercises):

                selected = exercises[choice - 1]

                break


            print(
                "Please select a valid exercise number."
            )


        except ValueError:

            print(
                "Please enter a number."
            )


    print("\nWhat do you want to change?")

    print("1. Sets")
    print("2. Reps")
    print("3. Weight")
    print("4. All")


    while True:

        option = input(
            "\nChoose option: "
        ).strip()


        if option in ["1", "2", "3", "4"]:

            break


        print(
            "Please choose 1, 2, 3, or 4."
        )


    # --------------------------------------------------------
    # CHANGE SETS
    # --------------------------------------------------------

    if option in ["1", "4"]:

        while True:

            try:

                new_sets = int(
                    input("New number of sets: ")
                )

                if new_sets > 0:

                    selected["sets"] = new_sets

                    break

                print(
                    "Sets must be greater than 0."
                )

            except ValueError:

                print(
                    "Please enter a whole number."
                )


    # --------------------------------------------------------
    # CHANGE REPS
    # --------------------------------------------------------

    if option in ["2", "4"]:

        while True:

            try:

                new_reps = int(
                    input("New target reps: ")
                )

                if new_reps >= 0:

                    selected["reps"] = new_reps

                    break

                print(
                    "Reps cannot be negative."
                )

            except ValueError:

                print(
                    "Please enter a whole number."
                )


    # --------------------------------------------------------
    # CHANGE WEIGHT
    # --------------------------------------------------------

    if option in ["3", "4"]:

        while True:

            try:

                new_weight = float(
                    input("New planned weight: ")
                )

                if new_weight >= 0:

                    selected["weight"] = new_weight

                    break

                print(
                    "Weight cannot be negative."
                )

            except ValueError:

                print(
                    "Please enter a valid number."
                )


    print("\nExercise updated successfully.")

    show_day_plan(day)


# ============================================================
# 2. REMOVE EXERCISE
# ============================================================

def remove_exercise(day):

    exercises = WORKOUT_PLAN[day]["exercises"]

    if not exercises:

        print("\nNo exercises available to remove.")

        return


    print("\n==========================================")
    print(f"REMOVE EXERCISE — {day}")
    print("==========================================")


    for number, exercise in enumerate(
        exercises,
        start=1
    ):

        print(
            f"{number}. {exercise['exercise_name']}"
        )


    while True:

        try:

            choice = int(
                input(
                    "\nSelect exercise number to remove: "
                )
            )


            if 1 <= choice <= len(exercises):

                break


            print(
                "Please select a valid exercise number."
            )


        except ValueError:

            print(
                "Please enter a number."
            )


    removed = exercises.pop(choice - 1)


    print(
        f"\n{removed['exercise_name']} "
        "removed successfully."
    )


# ============================================================
# 3. CHANGE BODY PARTS
# ============================================================
def edit_body_parts(day):

    while True:

        print("\n==========================================")
        print(f"BODY PARTS — {day}")
        print("==========================================")

        current_parts = WORKOUT_PLAN[day]["body_parts"]


        print("\nCurrent body parts:")

        if current_parts:

            for number, part in enumerate(
                current_parts,
                start=1
            ):
                print(f"{number}. {part}")

        else:

            print("None")


        print("\nOptions:")

        print("1. Add body part")
        print("2. Remove body part")
        print("3. Replace body parts")
        print("4. Back")


        choice = input(
            "\nChoose option: "
        ).strip()


        # ====================================================
        # ADD BODY PART
        # ====================================================

        if choice == "1":

            available_parts = [
                part
                for part in BODY_PARTS
                if part not in current_parts
            ]


            if not available_parts:

                print(
                    "\nAll available body parts "
                    "are already selected."
                )

                continue


            print("\nAvailable body parts:")

            for number, part in enumerate(
                available_parts,
                start=1
            ):
                print(
                    f"{number}. {part}"
                )


            selection = input(
                "\nEnter numbers to add "
                "(example: 1,3): "
            ).strip()


            try:

                numbers = [
                    int(x.strip())
                    for x in selection.split(",")
                ]


                added = []


                for number in numbers:

                    if (
                        1 <= number
                        <= len(available_parts)
                    ):

                        part = available_parts[
                            number - 1
                        ]

                        if part not in current_parts:

                            current_parts.append(part)

                            added.append(part)


                if added:

                    print(
                        "\nAdded:",
                        ", ".join(added)
                    )

                else:

                    print(
                        "\nNo valid body parts selected."
                    )


            except ValueError:

                print(
                    "\nPlease enter valid numbers."
                )


        # ====================================================
        # REMOVE BODY PART
        # ====================================================

        elif choice == "2":

            if not current_parts:

                print(
                    "\nThere are no body parts to remove."
                )

                continue


            print("\nCurrent body parts:")

            for number, part in enumerate(
                current_parts,
                start=1
            ):
                print(
                    f"{number}. {part}"
                )


            selection = input(
                "\nEnter numbers to remove "
                "(example: 1,3): "
            ).strip()


            try:

                numbers = [
                    int(x.strip())
                    for x in selection.split(",")
                ]


                removed = []


                for number in sorted(
                    numbers,
                    reverse=True
                ):

                    if (
                        1 <= number
                        <= len(current_parts)
                    ):

                        part = current_parts.pop(
                            number - 1
                        )

                        removed.append(part)


                if removed:

                    print(
                        "\nRemoved:",
                        ", ".join(removed)
                    )

                else:

                    print(
                        "\nNo valid body parts selected."
                    )


            except ValueError:

                print(
                    "\nPlease enter valid numbers."
                )


        # ====================================================
        # REPLACE BODY PARTS
        # ====================================================

        elif choice == "3":

            new_body_parts = select_body_parts()


            WORKOUT_PLAN[day][
                "body_parts"
            ] = new_body_parts


            print(
                "\nBody parts replaced successfully."
            )


        # ====================================================
        # BACK
        # ====================================================

        elif choice == "4":

            break


        else:

            print(
                "\nInvalid option."
            )



# ============================================================
# 4. ADD ANOTHER EXERCISE
# ============================================================

def add_another_exercise(day):

    print("\n==========================================")
    print(f"ADD EXERCISE — {day}")
    print("==========================================")


    add_exercise_to_day(day)


# ============================================================
# UPDATED DAY MANAGEMENT
# ============================================================


def manage_day(day):
    while True:
        print("\n==========================================")
        print(f"MANAGE {day.upper()}")
        print("==========================================")

        show_day_plan(day)

        print("\nOptions:")
        print("1. Add exercise")
        print("2. Edit exercise")
        print("3. Remove exercise")
        print("4. Change body parts")
        print("5. Save changes")
        print("6. Finish")

        choice = input("\nChoose option: ").strip()

        if choice == "1":
            add_another_exercise(day)

        elif choice == "2":
            edit_exercise(day)

        elif choice == "3":
            remove_exercise(day)

        elif choice == "4":
            edit_body_parts(day)

        elif choice == "5":
            save_day_plan(day)

        elif choice == "6":
            save_day_plan(day)
            break

        else:
            print("\nInvalid option.")



# ============================================================
# 6. EDIT ANY DAY OF THE WEEK
# ============================================================

def edit_weekly_plan():

    print("\n==========================================")
    print("EDIT WEEKLY PLAN")
    print("==========================================")


    while True:

        day = select_day()


        manage_day(day)


        another = input(
            "\nEdit another day? (yes/no): "
        ).lower().strip()


        if another != "yes":

            break
            
# ============================================================
# FITNESS APP
# PART 6 — WORKOUT LOGGER & WORKOUT HISTORY
# ============================================================


# ============================================================
# 1. ACTUAL WORKOUT HISTORY
# ============================================================

WORKOUT_HISTORY = []


# ============================================================
# 2. CREATE A NEW WORKOUT SESSION
# ============================================================

def create_workout_session(day, workout_type):

    session = {

        "day": day,

        "workout_type": workout_type,

        "date": None,

        "exercises": []

    }

    return session


# ============================================================
# EFFORT / RIR RATING (optional, per set)
# ============================================================

def prompt_for_effort():
    """Optional per-set effort rating: Easy / Medium / Hard, or skipped
    entirely (Enter). Returns 'easy', 'medium', 'hard', or None."""
    choice = input(
        "Effort (1=Easy, 2=Medium, 3=Hard, Enter to skip): "
    ).strip()

    if choice == "1":
        return "easy"
    elif choice == "2":
        return "medium"
    elif choice == "3":
        return "hard"
    else:
        return None  # not defined — falls back to the old rep-range rule


def compute_effective_credit(reps, effort):
    """The single source of truth for how much a set counts toward
    Effort Volume. Effort takes priority when provided; sets under 5
    reps never count toward volume regardless of effort (that's
    strength-territory, already fully credited in Strength Trend
    separately) — they're not ignored, just correctly categorized.
    No effort rating at all falls back to the original 5-20 rep rule."""
    if effort is None:
        return 1.0 if EFFECTIVE_REP_MIN <= reps <= EFFECTIVE_REP_MAX else 0.0

    if effort == "hard":
        return 1.0 if reps >= 5 else 0.0
    elif effort == "medium":
        return 0.7 if reps >= 5 else 0.0
    else:  # "easy"
        return 0.0


# ============================================================
# 3. LOG ONE EXERCISE
# ============================================================

def log_exercise(session, exercise_id, planned_data=None):

    exercise = EXERCISES[exercise_id]


    exercise_log = {

        "exercise_id": exercise_id,

        "exercise_name": exercise["name"],

        "planned": planned_data,

        "sets": []

    }


    print("\n==========================================")
    print(
        f"LOGGING: {exercise['name']}"
    )
    print("==========================================")


    # --------------------------------------------------------
    # NUMBER OF SETS
    # --------------------------------------------------------

    while True:

        try:

            number_of_sets = int(
                input(
                    "\nHow many sets did you perform? "
                )
            )

            if number_of_sets > 0:

                break

            print(
                "Number of sets must be greater than 0."
            )

        except ValueError:

            print(
                "Please enter a whole number."
            )


    # --------------------------------------------------------
    # LOG EACH INDIVIDUAL SET
    # --------------------------------------------------------

    for set_number in range(
        1,
        number_of_sets + 1
    ):

        print(
            f"\n--- Set {set_number} ---"
        )


        while True:

            try:

                reps = int(
                    input(
                        "Reps: "
                    )
                )

                if reps >= 0:

                    break

                print(
                    "Reps cannot be negative."
                )

            except ValueError:

                print(
                    "Please enter a whole number."
                )


        while True:

            try:

                weight = float(
                    input(
                        "Weight: "
                    )
                )

                if weight >= 0:

                    break

                print(
                    "Weight cannot be negative."
                )

            except ValueError:

                print(
                    "Please enter a valid number."
                )


        effort = prompt_for_effort()

        set_data = {

            "set_number": set_number,

            "reps": reps,

            "weight": weight,

            "effort": effort

        }


        exercise_log["sets"].append(
            set_data
        )


    session["exercises"].append(
        exercise_log
    )


    print("\nExercise logged successfully.")


# ============================================================
# 4. LOG AN EXERCISE FROM THE WEEKLY PLAN
# ============================================================

def log_planned_exercise(session, planned_exercise):

    exercise_id = planned_exercise["exercise_id"]


    log_exercise(

        session,

        exercise_id,

        planned_data={

            "sets": planned_exercise["sets"],

            "reps": planned_exercise["reps"],

            "weight": planned_exercise["weight"]

        }

    )


# ============================================================
# 5. START PLANNED ROUTINE
# ============================================================

def start_planned_routine(day):

    planned_exercises = (
        WORKOUT_PLAN[day]["exercises"]
    )


    if not planned_exercises:

        print("\n------------------------------------------")

        print(
            f"You don't have a workout plan for {day}."
        )

        print("------------------------------------------")

        return


    print("\n")
    print("##########################################")
    print(f"# START {day.upper()} ROUTINE")
    print("##########################################")


    session = create_workout_session(

        day,

        "planned"

    )


    print("\nToday's planned exercises:")


    for number, exercise in enumerate(

        planned_exercises,

        start=1

    ):

        print(

            f"{number}. "
            f"{exercise['exercise_name']} — "
            f"{exercise['sets']} × "
            f"{exercise['reps']} @ "
            f"{exercise['weight']}"

        )


    print("\nStarting workout...")


    # --------------------------------------------------------
    # LOG PLANNED EXERCISES
    # --------------------------------------------------------

    for planned_exercise in planned_exercises:

        print("\n")

        print(
            "=========================================="
        )

        print(
            f"NEXT EXERCISE: "
            f"{planned_exercise['exercise_name']}"
        )

        print(
            "=========================================="
        )


        log_planned_exercise(

            session,

            planned_exercise

        )


        # ----------------------------------------------------
        # USER CAN ADD AN EXTRA EXERCISE
        # ----------------------------------------------------

        while True:

            add_extra = input(

                "\nAdd another exercise? (yes/no): "

            ).lower().strip()


            if add_extra == "yes":

                selected_id = select_exercise()


                if selected_id is not None:

                    log_exercise(

                        session,

                        selected_id

                    )

                break


            elif add_extra == "no":

                break

            else:

                print(
                    "Please enter yes or no."
                )


    # --------------------------------------------------------
    # SAVE SESSION
    # --------------------------------------------------------

    finish_workout(session)


# ============================================================
# 6. START FREESTYLE WORKOUT
# ============================================================

def start_freestyle_workout(day):

    print("\n")
    print("##########################################")
    print("#       ADD EXERCISES DIRECTLY           #")
    print("##########################################")


    session = create_workout_session(

        day,

        "freestyle"

    )


    while True:

        print("\n------------------------------------------")

        print(
            "Search for an exercise to add."
        )

        print("------------------------------------------")


        selected_id = select_exercise()


        if selected_id is not None:

            log_exercise(

                session,

                selected_id

            )


        another = input(

            "\nAdd another exercise? (yes/no): "

        ).lower().strip()


        if another != "yes":

            break


    # --------------------------------------------------------
    # SAVE SESSION
    # --------------------------------------------------------

    if session["exercises"]:

        finish_workout(session)

    else:

        print(
            "\nNo exercises were logged."
        )


# ============================================================
# 7. FINISH WORKOUT
# ============================================================

def finish_workout(session):

    print("\n")
    print("##########################################")
    print("#          WORKOUT COMPLETED             #")
    print("##########################################")


    save_workout_session(session)


    print(
        "\nWorkout saved successfully."
    )


    print(
        f"Exercises completed: "
        f"{len(session['exercises'])}"
    )


    print(
        f"Workout type: "
        f"{session['workout_type']}"
    )


# ============================================================
# 8. SHOW TODAY'S WORKOUT SUMMARY
# ============================================================

def show_workout_summary(session):

    print("\n")
    print("==========================================")
    print("WORKOUT SUMMARY")
    print("==========================================")


    print(
        f"Day: {session['day']}"
    )

    print(
        f"Type: {session['workout_type']}"
    )


    for exercise in session["exercises"]:

        print("\n------------------------------------------")

        print(
            exercise["exercise_name"]
        )


        for set_data in exercise["sets"]:

            print(

                f"Set {set_data['set_number']}: "
                f"{set_data['reps']} reps × "
                f"{set_data['weight']}"

            )


    print("\n==========================================")


# ============================================================
# 9. WORKOUT HISTORY
# ============================================================

def show_workout_history():

    print("\n")
    print("##########################################")
    print("#          WORKOUT HISTORY               #")
    print("##########################################")


    if not WORKOUT_HISTORY:

        print(
            "\nNo workouts have been recorded yet."
        )

        return


    for workout_number, session in enumerate(

        WORKOUT_HISTORY,

        start=1

    ):

        print("\n------------------------------------------")

        print(
            f"Workout {workout_number}"
        )

        print(
            f"Day: {session['day']}"
        )

        print(
            f"Type: {session['workout_type']}"
        )


        for exercise in session["exercises"]:

            print(
                f"\n  {exercise['exercise_name']}"
            )


            for set_data in exercise["sets"]:

                print(

                    f"    Set "
                    f"{set_data['set_number']}: "
                    f"{set_data['reps']} reps × "
                    f"{set_data['weight']}"

                )


# ============================================================
# FITNESS APP
# PART 7A — DATABASE SETUP
# ============================================================

import sqlite3


# ============================================================
# 1. DATABASE FILE
# ============================================================

DATABASE_NAME = "fitness_app.db"


# ============================================================
# 2. CONNECT TO DATABASE
# ============================================================

import os

# Automatically forces the app to look in the exact folder where your code sits
PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))
DATABASE_NAME = os.path.join(PROJECT_FOLDER, "fitness_app.db")

def get_database_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection

#-------------------------
# ============================================================
# PART 11A — WORKOUT SESSION DATABASE
# ============================================================

def create_workout_history_tables():

    conn = sqlite3.connect("fitness_app.db")

    cursor = conn.cursor()


    # --------------------------------------------------------
    # WORKOUT SESSIONS
    # --------------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS workout_sessions (

            session_id INTEGER PRIMARY KEY AUTOINCREMENT,

            workout_date TEXT NOT NULL,

            workout_time TEXT NOT NULL,

            day_name TEXT NOT NULL,

            workout_type TEXT NOT NULL,

            created_at TEXT NOT NULL

        )
    """)


    # --------------------------------------------------------
    # EXERCISES PERFORMED IN A SESSION
    # --------------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS workout_session_exercises (

            session_exercise_id
                INTEGER PRIMARY KEY AUTOINCREMENT,

            session_id INTEGER NOT NULL,

            exercise_id INTEGER NOT NULL,

            exercise_name TEXT NOT NULL,

            exercise_order INTEGER NOT NULL,

            FOREIGN KEY (session_id)
                REFERENCES workout_sessions(session_id)

        )
    """)


    # --------------------------------------------------------
    # INDIVIDUAL SETS
    # --------------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS workout_sets (

            set_id INTEGER PRIMARY KEY AUTOINCREMENT,

            session_exercise_id INTEGER NOT NULL,

            set_number INTEGER NOT NULL,

            reps INTEGER NOT NULL,

            weight REAL NOT NULL,

            FOREIGN KEY (session_exercise_id)
                REFERENCES workout_session_exercises(
                    session_exercise_id
                )

        )
    """)


    conn.commit()

    conn.close()
# ============================================================
# PART 11B — BODY WEIGHT HISTORY
# ============================================================

def create_body_weight_table():

    conn = sqlite3.connect("fitness_app.db")

    cursor = conn.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS body_weight_history (

            weight_id INTEGER PRIMARY KEY AUTOINCREMENT,

            weight REAL NOT NULL,

            recorded_date TEXT NOT NULL,

            recorded_time TEXT NOT NULL,

            created_at TEXT NOT NULL

        )
    """)


    conn.commit()

    conn.close()

# ============================================================
# PART 11C — SAVE BODY WEIGHT
# ============================================================

def save_body_weight(weight):

    now = datetime.now()


    recorded_date = now.strftime(
        "%Y-%m-%d"
    )

    recorded_time = now.strftime(
        "%H:%M:%S"
    )

    created_at = now.isoformat()


    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()


    cursor.execute("""
        INSERT INTO body_weight_history (

            weight,
            recorded_date,
            recorded_time,
            created_at

        )

        VALUES (?, ?, ?, ?)

    """, (

        weight,
        recorded_date,
        recorded_time,
        created_at

    ))


    conn.commit()

    conn.close()


    print(
        f"\nBody weight {weight} kg saved."
    )


# ============================================================
# 3. CREATE DATABASE TABLES
# ============================================================

def initialize_database():

    connection = get_database_connection()

    cursor = connection.cursor()


    # --------------------------------------------------------
    # USER PROFILE
    # --------------------------------------------------------

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS user_profile (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            age INTEGER,

            height REAL,

            body_weight REAL,

            goal TEXT,

            gender TEXT

        )

    """)

    # Migration: existing databases created before the gender column
    # existed won't have it yet. CREATE TABLE IF NOT EXISTS above won't
    # add it to an already-existing table, so add it safely here.
    try:
        cursor.execute("ALTER TABLE user_profile ADD COLUMN gender TEXT")
    except sqlite3.OperationalError:
        pass  # column already exists — nothing to do


    # --------------------------------------------------------
    # WORKOUT PLANS
    # --------------------------------------------------------

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS workout_plans (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            day TEXT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )

    """)


    # --------------------------------------------------------
    # PLANNED EXERCISES
    # --------------------------------------------------------

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS planned_exercises (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            plan_id INTEGER NOT NULL,

            exercise_id TEXT NOT NULL,

            exercise_name TEXT NOT NULL,

            sets INTEGER NOT NULL,

            reps INTEGER NOT NULL,

            weight REAL NOT NULL,

            FOREIGN KEY (plan_id)

                REFERENCES workout_plans(id)

        )

    """)


    # --------------------------------------------------------
    # WORKOUT SESSIONS
    # --------------------------------------------------------

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS workout_sessions (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            day TEXT NOT NULL,

            workout_type TEXT NOT NULL,

            workout_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )

    """)


    # --------------------------------------------------------
    # PERFORMED EXERCISES
    # --------------------------------------------------------

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS performed_exercises (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            session_id INTEGER NOT NULL,

            exercise_id TEXT NOT NULL,

            exercise_name TEXT NOT NULL,

            FOREIGN KEY (session_id)

                REFERENCES workout_sessions(id)

        )

    """)


    # --------------------------------------------------------
    # INDIVIDUAL SETS
    # --------------------------------------------------------

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS performed_sets (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            performed_exercise_id INTEGER NOT NULL,

            set_number INTEGER NOT NULL,

            reps INTEGER NOT NULL,

            weight REAL NOT NULL,

            effort TEXT,

            FOREIGN KEY (performed_exercise_id)

                REFERENCES performed_exercises(id)

        )

    """)

    # Migration: existing databases created before the effort column
    # existed won't have it yet. CREATE TABLE IF NOT EXISTS above won't
    # add it to an already-existing table, so add it safely here.
    try:
        cursor.execute("ALTER TABLE performed_sets ADD COLUMN effort TEXT")
    except sqlite3.OperationalError:
        pass  # column already exists — nothing to do


    # --------------------------------------------------------
    # TRAINING RESETS ("Starting Again")
    # A reset never deletes any prior data — it just records the date
    # so block boundaries and personal-best lookups know where the
    # current training era begins. Old data stays queryable for future
    # comparison-across-eras features.
    # --------------------------------------------------------

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS training_resets (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            reset_date TEXT NOT NULL

        )

    """)


    connection.commit()

    connection.close()
# ============================================================
# PART 7B — USER PROFILE STORAGE
# ============================================================


def save_user_profile(
    age,
    height,
    body_weight,
    goal,
    gender=None
):

    connection = get_database_connection()

    cursor = connection.cursor()


    cursor.execute("""

        INSERT INTO user_profile (

            age,
            height,
            body_weight,
            goal,
            gender

        )

        VALUES (?, ?, ?, ?, ?)

    """, (

        age,
        height,
        body_weight,
        goal,
        gender

    ))


    connection.commit()

    connection.close()


# ============================================================
# LOAD USER PROFILE
# ============================================================

def load_user_profile():

    connection = get_database_connection()

    cursor = connection.cursor()


    cursor.execute("""

        SELECT *

        FROM user_profile

        ORDER BY id DESC

        LIMIT 1

    """)


    profile = cursor.fetchone()


    connection.close()


    if profile is None:

        return None


    return dict(profile)
# ============================================================
# PART 7C — WORKOUT SESSION STORAGE
# ============================================================


def save_workout_session(session):

    connection = get_database_connection()

    cursor = connection.cursor()


    # --------------------------------------------------------
    # CREATE WORKOUT SESSION
    # --------------------------------------------------------

    cursor.execute("""

        INSERT INTO workout_sessions (

            day,
            workout_type

        )

        VALUES (?, ?)

    """, (

        session["day"],

        session["workout_type"]

    ))


    session_id = cursor.lastrowid


    # --------------------------------------------------------
    # SAVE EVERY EXERCISE
    # --------------------------------------------------------

    for exercise in session["exercises"]:


        cursor.execute("""

            INSERT INTO performed_exercises (

                session_id,
                exercise_id,
                exercise_name

            )

            VALUES (?, ?, ?)

        """, (

            session_id,

            exercise["exercise_id"],

            exercise["exercise_name"]

        ))


        performed_exercise_id = cursor.lastrowid


        # ----------------------------------------------------
        # SAVE EVERY INDIVIDUAL SET
        # ----------------------------------------------------

        for set_data in exercise["sets"]:

            cursor.execute("""

                INSERT INTO performed_sets (

                    performed_exercise_id,
                    set_number,
                    reps,
                    weight,
                    effort

                )

                VALUES (?, ?, ?, ?, ?)

            """, (

                performed_exercise_id,

                set_data["set_number"],

                set_data["reps"],

                set_data["weight"],

                set_data.get("effort")

            ))


    connection.commit()

    connection.close()
# ============================================================
# PART 7D — LOAD WORKOUT HISTORY
# ============================================================


def load_workout_history():

    connection = get_database_connection()

    cursor = connection.cursor()


    cursor.execute("""

        SELECT *

        FROM workout_sessions

        ORDER BY workout_date ASC

    """)


    sessions = cursor.fetchall()


    workout_history = []


    for session_row in sessions:


        session = {

            "id": session_row["id"],

            "day": session_row["day"],

            "workout_type": session_row["workout_type"],

            "date": session_row["workout_date"],

            "exercises": []

        }


        cursor.execute("""

            SELECT *

            FROM performed_exercises

            WHERE session_id = ?

            ORDER BY id

        """, (

            session_row["id"],

        ))


        exercises = cursor.fetchall()


        for exercise_row in exercises:


            exercise = {

                "exercise_id":
                    exercise_row["exercise_id"],

                "exercise_name":
                    exercise_row["exercise_name"],

                "sets": []

            }


            cursor.execute("""

                SELECT *

                FROM performed_sets

                WHERE performed_exercise_id = ?

                ORDER BY set_number

            """, (

                exercise_row["id"],

            ))


            sets = cursor.fetchall()


            for set_row in sets:

                exercise["sets"].append({

                    "set_number":
                        set_row["set_number"],

                    "reps":
                        set_row["reps"],

                    "weight":
                        set_row["weight"]

                })


            session["exercises"].append(
                exercise
            )


        workout_history.append(
            session
        )


    connection.close()


    return workout_history
# ============================================================
# DATABASE INITIALIZATION
# ============================================================

initialize_database()
# ============================================================
# FITNESS APP
# PART 8A — BODY PART STORAGE
# ============================================================


def initialize_plan_database():

    connection = get_database_connection()

    cursor = connection.cursor()


    # --------------------------------------------------------
    # BODY PARTS FOR EACH WORKOUT PLAN
    # --------------------------------------------------------

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS plan_body_parts (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            plan_id INTEGER NOT NULL,

            body_part TEXT NOT NULL,

            FOREIGN KEY (plan_id)

                REFERENCES workout_plans(id)

        )

    """)


    connection.commit()

    connection.close()
# ============================================================
# PART 8B — SAVE ONE DAY'S PLAN
# ============================================================


def save_day_plan(day):

    connection = get_database_connection()

    cursor = connection.cursor()


    # --------------------------------------------------------
    # REMOVE OLD PLAN FOR THIS DAY
    # --------------------------------------------------------

    cursor.execute("""

        SELECT id

        FROM workout_plans

        WHERE day = ?

    """, (day,))


    old_plan = cursor.fetchone()


    if old_plan:

        old_plan_id = old_plan["id"]


        cursor.execute("""

            DELETE FROM plan_body_parts

            WHERE plan_id = ?

        """, (old_plan_id,))


        cursor.execute("""

            DELETE FROM planned_exercises

            WHERE plan_id = ?

        """, (old_plan_id,))


        cursor.execute("""

            DELETE FROM workout_plans

            WHERE id = ?

        """, (old_plan_id,))


    # --------------------------------------------------------
    # CREATE NEW PLAN
    # --------------------------------------------------------

    cursor.execute("""

        INSERT INTO workout_plans (day)

        VALUES (?)

    """, (day,))


    plan_id = cursor.lastrowid


    # --------------------------------------------------------
    # SAVE BODY PARTS
    # --------------------------------------------------------

    for body_part in WORKOUT_PLAN[day]["body_parts"]:

        cursor.execute("""

            INSERT INTO plan_body_parts (

                plan_id,
                body_part

            )

            VALUES (?, ?)

        """, (

            plan_id,
            body_part

        ))


    # --------------------------------------------------------
    # SAVE PLANNED EXERCISES
    # --------------------------------------------------------

    for exercise in WORKOUT_PLAN[day]["exercises"]:

        cursor.execute("""

            INSERT INTO planned_exercises (

                plan_id,
                exercise_id,
                exercise_name,
                sets,
                reps,
                weight

            )

            VALUES (?, ?, ?, ?, ?, ?)

        """, (

            plan_id,

            exercise["exercise_id"],

            exercise["exercise_name"],

            exercise["sets"],

            exercise["reps"],

            exercise["weight"]

        ))


    connection.commit()

    connection.close()


    print(
        f"\n{day} plan saved successfully."
    )
# ============================================================
# PART 8C — LOAD WEEKLY PLAN FROM DATABASE
# ============================================================


def load_workout_plan():

    connection = get_database_connection()

    cursor = connection.cursor()


    # --------------------------------------------------------
    # CLEAR CURRENT MEMORY PLAN
    # --------------------------------------------------------

    for day in DAYS:

        WORKOUT_PLAN[day]["body_parts"] = []

        WORKOUT_PLAN[day]["exercises"] = []


    # --------------------------------------------------------
    # LOAD EACH DAY
    # --------------------------------------------------------

    cursor.execute("""

        SELECT *

        FROM workout_plans

        ORDER BY id

    """)


    plans = cursor.fetchall()


    for plan in plans:

        day = plan["day"]

        plan_id = plan["id"]


        # ----------------------------------------------------
        # LOAD BODY PARTS
        # ----------------------------------------------------

        cursor.execute("""

            SELECT body_part

            FROM plan_body_parts

            WHERE plan_id = ?

            ORDER BY id

        """, (plan_id,))


        body_parts = cursor.fetchall()


        for body_part in body_parts:

            WORKOUT_PLAN[day]["body_parts"].append(

                body_part["body_part"]

            )


        # ----------------------------------------------------
        # LOAD EXERCISES
        # ----------------------------------------------------

        cursor.execute("""

            SELECT *

            FROM planned_exercises

            WHERE plan_id = ?

            ORDER BY id

        """, (plan_id,))


        exercises = cursor.fetchall()


        for exercise in exercises:

            WORKOUT_PLAN[day]["exercises"].append({

                "exercise_id":
                    exercise["exercise_id"],

                "exercise_name":
                    exercise["exercise_name"],

                "sets":
                    exercise["sets"],

                "reps":
                    exercise["reps"],

                "weight":
                    exercise["weight"]

            })


    connection.close()
# ============================================================
# LOAD SAVED WORKOUT PLAN
# ============================================================

# 1. Create the database files and empty tables first
initialize_database()
initialize_plan_database()

# 2. Load any existing user workout data into the app memory
load_workout_plan()

# 3. Start the actual interactive application loop
#workout_plan_builder()

    
# ============================================================
# PART 9A — GET TODAY'S DAY
# ============================================================

def get_today_day():

    return datetime.now().strftime("%A")

# ============================================================
# PART 9B — START TODAY'S WORKOUT PLAN
# ============================================================
def create_session_from_plan(day):
    """
    Creates an active, copyable layout of the user's weekly routine 
    for tracking current workout sets.
    """
    import copy
    
    plan = WORKOUT_PLAN[day]
    
    session_data = {
        "day": day,
        "workout_type": "planned",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "exercises": []
    }
    
    for exercise in plan.get("exercises", []):
        session_data["exercises"].append(copy.deepcopy(exercise))
        
    return session_data
 #============================================================
# PART 9A — START TODAY'S WORKOUT PLAN
# ============================================================

def start_todays_workout_plan():

    today = get_today_day()

    print("\n")
    print("##########################################")
    print("#       START TODAY'S WORKOUT            #")
    print("##########################################")

    print(f"\nToday: {today}")


    # --------------------------------------------------------
    # CHECK WEEKLY PLAN
    # --------------------------------------------------------

    today_plan = WORKOUT_PLAN.get(today)


    if not today_plan:

        print(
            f"\nNo workout plan found for {today}."
        )

        print(
            "\nReturning to Start Workout menu..."
        )

        return


    if not today_plan["exercises"]:

        print(
            f"\nYou don't have any exercises "
            f"planned for {today}."
        )

        print(
            "\nReturning to Start Workout menu..."
        )

        return


    # --------------------------------------------------------
    # CREATE A SEPARATE TODAY SESSION
    # --------------------------------------------------------

    session = create_session_from_plan(
        today
    )


    print(
        f"\n{today}'s workout plan loaded."
    )


    # --------------------------------------------------------
    # OPEN TODAY'S WORKOUT SCREEN
    # --------------------------------------------------------

    todays_workout_screen(
        session
    )
# ============================================================
# PART 9B — TODAY'S WORKOUT SCREEN
# ============================================================

def todays_workout_screen(session):

    while True:

        print("\n")
        print("##########################################")
        print(
            f"#          {session['day'].upper()} WORKOUT"
        )
        print("##########################################")


        # ----------------------------------------------------
        # SHOW EXERCISES
        # ----------------------------------------------------

        if session["exercises"]:

            print("\nExercises:")

            for number, exercise in enumerate(

                session["exercises"],

                start=1

            ):

                print(
                    f"{number}. "
                    f"{exercise['exercise_name']}"
                )

        else:

            print(
                "\nNo exercises in today's workout."
            )


        # ----------------------------------------------------
        # OPTIONS
        # ----------------------------------------------------

        print("\n")

        print("A. Select Exercise")

        print("B. Add Exercise")

        print("C. Finish Workout")

        print("D. Exit Workout")


        choice = input(
            "\nChoose option: "
        ).strip().lower()


        # ----------------------------------------------------
        # SELECT EXISTING EXERCISE
        # ----------------------------------------------------

        if choice == "a":

            if not session["exercises"]:

                print(
                    "\nNo exercises available."
                )

                continue


            select_and_log_exercise(
                session
            )


        # ----------------------------------------------------
        # ADD NEW EXERCISE
        # ----------------------------------------------------

        elif choice == "b":

            add_exercise_to_session(
                session
            )


        # ----------------------------------------------------
        # FINISH
        # ----------------------------------------------------

        elif choice == "c":

            if not session["exercises"]:

                print(
                    "\nNo exercises have been added."
                )

                continue


            finish_logged_workout(
                session
            )

            break


        # ----------------------------------------------------
        # EXIT WITHOUT SAVING
        # ----------------------------------------------------

        elif choice == "d":

            confirm = input(
                "\nExit workout without saving? "
                "(yes/no): "
            ).lower().strip()


            if confirm == "yes":

                print(
                    "\nWorkout discarded."
                )

                break


        else:

            print(
                "\nInvalid option."
            )
# ============================================================
# PART 9C — SELECT AND LOG EXERCISE
# ============================================================

def select_and_log_exercise(session):

    print("\n")
    print("==========================================")
    print("SELECT EXERCISE")
    print("==========================================")


    for number, exercise in enumerate(

        session["exercises"],

        start=1

    ):

        print(
            f"{number}. "
            f"{exercise['exercise_name']}"
        )


    while True:

        try:

            choice = int(
                input(
                    "\nSelect exercise number: "
                )
            )


            if 1 <= choice <= len(
                session["exercises"]
            ):

                break


            print(
                "\nInvalid exercise number."
            )


        except ValueError:

            print(
                "\nPlease enter a number."
            )


    selected_exercise = session[
        "exercises"
    ][choice - 1]


    log_planned_exercise(session,
        selected_exercise
    )

# ============================================================
# PART 9C — ADD WORKOUT
# ============================================================
# ============================================================
# ADD EXERCISE TO TODAY'S WORKOUT SESSION
# ============================================================

# ============================================================
# ADD EXERCISE TO TODAY'S WORKOUT SESSION
# ============================================================

# ============================================================
# PART 13A — ADD EXERCISE TO WORKOUT SESSION
# SET-BY-SET LOGGING
# ============================================================

# ============================================================
# PART 13D-1 — ADD EXERCISE TO WORKOUT SESSION
# ============================================================

def add_exercise_to_session(session):

    print("\n==========================================")
    print("ADD EXERCISE TO TODAY'S WORKOUT")
    print("==========================================")


    selected_id = select_exercise()


    if selected_id is None:

        return False


    exercise = EXERCISES[selected_id]


    exercise_data = {

        "exercise_id": selected_id,

        "exercise_name": exercise["name"],

        "sets": []

    }


    # --------------------------------------------------------
    # NUMBER OF SETS
    # --------------------------------------------------------

    while True:

        try:

            number_of_sets = int(
                input(
                    "\nHow many sets did you perform? "
                )
            )


            if number_of_sets > 0:

                break


            print(
                "Number of sets must be greater than 0."
            )


        except ValueError:

            print(
                "Please enter a whole number."
            )


    # --------------------------------------------------------
    # LOG EACH SET
    # --------------------------------------------------------

    for set_number in range(
        1,
        number_of_sets + 1
    ):

        print(
            f"\n---------- SET {set_number} ----------"
        )


        while True:

            try:

                reps = int(
                    input(
                        "Reps: "
                    )
                )


                if reps >= 0:

                    break


                print(
                    "Reps cannot be negative."
                )


            except ValueError:

                print(
                    "Please enter a whole number."
                )


        while True:

            try:

                weight = float(
                    input(
                        "Weight (kg): "
                    )
                )


                if weight >= 0:

                    break


                print(
                    "Weight cannot be negative."
                )


            except ValueError:

                print(
                    "Please enter a valid number."
                )


        effort = prompt_for_effort()

        exercise_data["sets"].append({

            "set_number": set_number,

            "reps": reps,

            "weight": weight,

            "effort": effort

        })


    session["exercises"].append(
        exercise_data
    )


    print("\n==========================================")

    print(
        f"{exercise['name']} added "
        "to today's workout."
    )


    print("\nLogged sets:")


    for workout_set in exercise_data["sets"]:

        print(
            f"Set {workout_set['set_number']}: "
            f"{workout_set['reps']} reps × "
            f"{workout_set['weight']} kg"
        )


    print("==========================================")


    return True
    
# ============================================================
# PART 13D-2 — ADD SET
# ============================================================

def add_set_to_exercise(exercise):

    set_number = len(
        exercise["sets"]
    ) + 1


    print(
        f"\n---------- SET {set_number} ----------"
    )


    # --------------------------------------------------------
    # REPS
    # --------------------------------------------------------

    while True:

        try:

            reps = int(
                input(
                    "Reps: "
                )
            )


            if reps >= 0:

                break


            print(
                "Reps cannot be negative."
            )


        except ValueError:

            print(
                "Please enter a whole number."
            )


    # --------------------------------------------------------
    # WEIGHT
    # --------------------------------------------------------

    while True:

        try:

            weight = float(
                input(
                    "Weight (kg): "
                )
            )


            if weight >= 0:

                break


            print(
                "Weight cannot be negative."
            )


        except ValueError:

            print(
                "Please enter a valid number."
            )


    effort = prompt_for_effort()

    exercise["sets"].append({

        "set_number": set_number,

        "reps": reps,

        "weight": weight,

        "effort": effort

    })


    print(
        f"\nSet {set_number} added."
    )

# ============================================================
# PART 13D-3 — EDIT SET
# ============================================================

def edit_set(exercise):

    if not exercise["sets"]:

        print(
            "\nNo sets available."
        )

        return


    print(
        f"\n{exercise['exercise_name']}"
    )


    for workout_set in exercise["sets"]:

        print(
            f"{workout_set['set_number']}. "
            f"{workout_set['reps']} reps × "
            f"{workout_set['weight']} kg"
        )


    try:

        choice = int(
            input(
                "\nSelect set to edit: "
            )
        )


        if not (
            1 <= choice
            <= len(exercise["sets"])
        ):

            print(
                "\nInvalid set."
            )

            return


    except ValueError:

        print(
            "\nPlease enter a number."
        )

        return


    selected_set = exercise[
        "sets"
    ][choice - 1]


    # --------------------------------------------------------
    # NEW REPS
    # --------------------------------------------------------

    while True:

        try:

            reps = int(
                input(
                    "New reps: "
                )
            )


            if reps >= 0:

                break


            print(
                "Reps cannot be negative."
            )


        except ValueError:

            print(
                "Please enter a whole number."
            )


    # --------------------------------------------------------
    # NEW WEIGHT
    # --------------------------------------------------------

    while True:

        try:

            weight = float(
                input(
                    "New weight (kg): "
                )
            )


            if weight >= 0:

                break


            print(
                "Weight cannot be negative."
            )


        except ValueError:

            print(
                "Please enter a valid number."
            )


    selected_set["reps"] = reps

    selected_set["weight"] = weight


    print(
        "\nSet updated successfully."
    )

# ============================================================
# PART 13D-4 — REMOVE SET
# ============================================================

def remove_set(exercise):

    if not exercise["sets"]:

        print(
            "\nNo sets available."
        )

        return


    print(
        f"\n{exercise['exercise_name']}"
    )


    for workout_set in exercise["sets"]:

        print(
            f"{workout_set['set_number']}. "
            f"{workout_set['reps']} reps × "
            f"{workout_set['weight']} kg"
        )


    try:

        choice = int(
            input(
                "\nSelect set to remove: "
            )
        )


        if not (
            1 <= choice
            <= len(exercise["sets"])
        ):

            print(
                "\nInvalid set."
            )

            return


    except ValueError:

        print(
            "\nPlease enter a number."
        )

        return


    removed_set = exercise[
        "sets"
    ].pop(choice - 1)


    # --------------------------------------------------------
    # RE-NUMBER REMAINING SETS
    # --------------------------------------------------------

    for number, workout_set in enumerate(

        exercise["sets"],

        start=1

    ):

        workout_set["set_number"] = number


    print(
    "\nSet removed successfully.")

# ============================================================
# PART 13D-5 — EDIT EXERCISE
# ============================================================

def edit_workout_exercise(session):

    if not session["exercises"]:

        print(
            "\nNo exercises available."
        )

        return


    print("\nToday's Exercises:")


    for number, exercise in enumerate(

        session["exercises"],

        start=1

    ):

        print(
            f"{number}. "
            f"{exercise['exercise_name']}"
        )


    try:

        choice = int(
            input(
                "\nSelect exercise: "
            )
        )


        if not (
            1 <= choice
            <= len(session["exercises"])
        ):

            print(
                "\nInvalid exercise."
            )

            return


    except ValueError:

        print(
            "\nPlease enter a number."
        )

        return


    exercise = session[
        "exercises"
    ][choice - 1]


    while True:

        print("\n==========================================")

        print(
            exercise["exercise_name"]
        )

        print("==========================================")


        if exercise["sets"]:

            for workout_set in exercise["sets"]:

                print(
                    f"Set {workout_set['set_number']}: "
                    f"{workout_set['reps']} reps × "
                    f"{workout_set['weight']} kg"
                )

        else:

            print("No sets.")


        print("\nOptions:")

        print("1. Add Set")
        print("2. Edit Set")
        print("3. Remove Set")
        print("4. Back")


        option = input(
            "\nChoose option: "
        ).strip()


        if option == "1":

            add_set_to_exercise(
                exercise
            )


        elif option == "2":

            edit_set(
                exercise
            )


        elif option == "3":

            remove_set(
                exercise
            )


        elif option == "4":

            break


        else:

            print(
                "\nInvalid option."
            )

# ============================================================
# PART 13B — FINISH AND SAVE WORKOUT
# ============================================================

def finish_logged_workout(session):

    connection = get_database_connection()

    cursor = connection.cursor()


    try:

        # ----------------------------------------------------
        # SAVE WORKOUT SESSION
        # ----------------------------------------------------

        cursor.execute("""
            INSERT INTO workout_sessions (
                day,
                workout_type,
                workout_date
            )

            VALUES (?, ?, ?)
        """, (

            session["day"],

            session["workout_type"],

            f"{session['date']} {session['time']}"

        ))


        session_id = cursor.lastrowid


        # ----------------------------------------------------
        # SAVE EACH EXERCISE
        # ----------------------------------------------------

        for exercise in session["exercises"]:

            cursor.execute("""
                INSERT INTO performed_exercises (
                    session_id,
                    exercise_id,
                    exercise_name
                )

                VALUES (?, ?, ?)
            """, (

                session_id,

                exercise["exercise_id"],

                exercise["exercise_name"]

            ))


            performed_exercise_id = (
                cursor.lastrowid
            )


            # ------------------------------------------------
            # SAVE EACH INDIVIDUAL SET
            # ------------------------------------------------

            for workout_set in exercise["sets"]:

                cursor.execute("""
                    INSERT INTO performed_sets (
                        performed_exercise_id,
                        set_number,
                        reps,
                        weight,
                        effort
                    )

                    VALUES (?, ?, ?, ?, ?)
                """, (

                    performed_exercise_id,

                    workout_set["set_number"],

                    workout_set["reps"],

                    workout_set["weight"],

                    workout_set.get("effort")

                ))


        # ----------------------------------------------------
        # COMMIT EVERYTHING
        # ----------------------------------------------------

        connection.commit()


        print("\n")
        print("##########################################")
        print("#         WORKOUT SAVED SUCCESSFULLY     #")
        print("##########################################")


        print(
            f"\nDate: {session['date']}"
        )

        print(
            f"Time: {session['time']}"
        )

        print(
            f"Workout type: "
            f"{session['workout_type']}"
        )


        print(
            "\nYour workout has been saved."
        )


    except Exception as error:

        # ----------------------------------------------------
        # ROLLBACK IF ANYTHING GOES WRONG
        # ----------------------------------------------------

        connection.rollback()


        print("\n")
        print("##########################################")
        print("#          WORKOUT SAVE FAILED           #")
        print("##########################################")


        print(
            f"\nError: {error}"
        )


    finally:

        connection.close()

# ============================================================
# PART 9 — ADD WORKOUT WITHOUT WEEKLY PLAN

def remove_exercise_from_session(session):
    """
    Removes an exercise track entirely from the active workout session state.
    """
    if not session["exercises"]:
        print("\nNo exercises inside today's session log to remove.")
        return

    print("\nSelect exercise to remove:")
    for i, ex in enumerate(session["exercises"], start=1):
        print(f"{i}. {ex['exercise_name']}")

    try:
        choice = int(input("\nSelect exercise number: "))
        if 1 <= choice <= len(session["exercises"]):
            removed = session["exercises"].pop(choice - 1)
            print(f"\n{removed['exercise_name']} removed from current session.")
        else:
            print("\nInvalid selection number.")
    except ValueError:
        print("\nPlease type a valid numeric value.")


# ============================================================

def add_workout():
    today = get_today_day()
    session = {
        "day": today,
        "workout_type": "freestyle",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "exercises": []
    }

    while True:
        print("\n")
        print("##########################################")
        print("#              ADD WORKOUT               #")
        print("##########################################")
        print(f"\nToday: {today}")

        # ----------------------------------------------------
        # SHOW CURRENT EXERCISES
        # ----------------------------------------------------
        if session["exercises"]:
            print("\nToday's Exercises:")
            for number, exercise in enumerate(session["exercises"], start=1):
                print(f"{number}. {exercise['exercise_name']}")
        else:
            print("\nNo exercises added yet.")

        # ----------------------------------------------------
        # OPTIONS
        # ----------------------------------------------------
        print("\n1. Add Exercise")
        print("2. Edit Exercise")
        print("3. Remove Exercise")
        print("4. Finish Workout")
        print("5. Exit")

        choice = input("\nChoose option: ").strip()

        # ----------------------------------------------------
        # MENU SELECTION HANDLING
        # ----------------------------------------------------
        if choice == "1":
            add_exercise_to_session(session)

        elif choice == "2":
            edit_workout_exercise(session)

        elif choice == "3":
            remove_exercise_from_session(session)

        elif choice == "4":
            if not session["exercises"]:
                print(
                    "\nYou must add at least "
                    "one exercise first."
                )
                continue
            finish_logged_workout(session)
            break

        elif choice == "5":
            confirm = input(
                "\nExit without saving? (yes/no): "
            ).lower().strip()
            if confirm == "yes":
                print("\nWorkout cancelled.")
                break



# ============================================================
# PART 9D — WORKOUT LOGGER
# ============================================================

# ============================================================
# PART 13D-6 — EDITABLE WORKOUT LOGGER
# ============================================================

def workout_logger(session):

    while True:

        print("\n")
        print("==========================================")
        print("             WORKOUT LOGGER")
        print("==========================================")


        # ----------------------------------------------------
        # SHOW CURRENT WORKOUT
        # ----------------------------------------------------

        if session["exercises"]:

            show_workout_summary(session)
                
            

        else:

            print(
                "\nNo exercises added yet."
            )


        print("\nOptions:")

        print("1. Edit exercise")
        print("2. Add exercise")
        print("3. Remove exercise")
        print("4. Finish workout")
        print("5. Cancel workout")


        choice = input(
            "\nChoose option: "
        ).strip()


        # ----------------------------------------------------
        # EDIT EXERCISE
        # ----------------------------------------------------

        if choice == "1":

            edit_workout_exercise(
                session
            )


        # ----------------------------------------------------
        # ADD EXERCISE
        # ----------------------------------------------------

        elif choice == "2":

            add_exercise_to_session(
                session
            )


        # ----------------------------------------------------
        # REMOVE EXERCISE
        # ----------------------------------------------------

        elif choice == "3":

            remove_exercise_from_session(
                session
            )


        # ----------------------------------------------------
        # FINISH WORKOUT
        # ----------------------------------------------------

        elif choice == "4":

            if not session["exercises"]:

                print(
                    "\nYou haven't added "
                    "any exercises."
                )

                continue


            finish_logged_workout(
                session
            )

            break


        # ----------------------------------------------------
        # CANCEL WORKOUT
        # ----------------------------------------------------

        elif choice == "5":

            confirm = input(
                "\nCancel this workout? "
                "(yes/no): "
            ).lower().strip()


            if confirm == "yes":

                print(
                    "\nWorkout cancelled."
                )

                break


        else:

            print(
                "\nInvalid option."
            )
# ============================================================
# PART 10B — MAIN APPLICATION MENU
# ============================================================
# ==========================================================
# PART 11D - VIEW BODY WEIGHT HISTORY
# ==========================================================

def view_body_weight_history():
    # Make sure to change 'fitness_app.db' if you aren't using DB_NAME
    conn = sqlite3.connect('fitness_app.db')
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT 
            weight,
            recorded_date,
            recorded_time
        FROM body_weight_history
        ORDER BY 
            recorded_date ASC,
            recorded_time ASC
    """)
    
    records = cursor.fetchall()
    conn.close()
    
    print("\n")
    print("##########################################")
    print("#           BODY WEIGHT HISTORY          #")
    print("##########################################")
    
    if not records:
        print("\nNo body weight records found.")
        return
        
    for row in records:
        # Note: If fetchall returns sqlite3.Row or tuples, 
        # using indexing works best:
        weight = row[0]
        date = row[1]
        time = row[2]
        print(f"\n{date} {time}")
        print(f"Weight: {weight} kg")
# ==========================================================
# USER PROFILE INTERFACE AND DASHBOARD
# ==========================================================
def create_profile_interface():
    connection = get_database_connection()
    cursor = connection.cursor()
    
    # FIX: Fetch the absolute LATEST entry in the database table instead of the frozen first row
    cursor.execute("SELECT id, age, height, body_weight, goal, gender FROM user_profile ORDER BY id DESC LIMIT 1")
    profile = cursor.fetchone()
    
    # Establish dynamic defaults from database context states
    current_age = str(profile["age"]) if profile else ""
    current_height = str(profile["height"]) if profile else ""
    current_weight = str(profile["body_weight"]) if profile else ""
    current_goal = str(profile["goal"]).strip() if profile and profile["goal"] else "Not Set"
    current_gender = str(profile["gender"]).strip() if profile and profile["gender"] else "Not Set"

    # Show the User Profile Card Dashboard Screen
    print("\n==========================================")
    print("             USER PROFILE                 ")
    print("==========================================")
    print(f"Age:    {current_age if current_age else 'Not Set'} years")
    print(f"Gender: {current_gender}")
    print(f"Height: {current_height if current_height else 'Not Set'} cm")
    print(f"Weight: {current_weight if current_weight else 'Not Set'} kg")
    print(f"Goal:   {current_goal}")
    print("==========================================")
    print("Options:")
    print("1. Update Profile Info & Goal")
    print("2. Back to Main Menu")
    
    choice = input("\nChoose option: ").strip()
    
    if choice == "1":
        print("\n--- Update Profile (Press Enter to keep current value) ---")
        
        new_age = input(f"Enter your age [{current_age}]: ").strip()
        age = int(new_age) if new_age != "" else (int(current_age) if current_age else None)

        new_gender = input(f"Enter your gender [{current_gender}]: ").strip()
        gender = new_gender if new_gender != "" else (current_gender if current_gender != "Not Set" else None)
        
        new_height = input(f"Enter your height in cm [{current_height}]: ").strip()
        height = float(new_height) if new_height != "" else (float(current_height) if current_height else None)
        
        new_weight = input(f"Enter your body weight in kg [{current_weight}]: ").strip()
        weight = float(new_weight) if new_weight != "" else (float(current_weight) if current_weight else None)
        
        new_goal = input(f"Enter your goal (free text) [{current_goal}]: ").strip()
        selected_goal = new_goal if new_goal != "" else (current_goal if current_goal != "Not Set" else None)
        
        # FIX: Explicitly perform an UPDATE if editing a row, otherwise insert the first user seed row
        if profile:
            cursor.execute("""
                UPDATE user_profile 
                SET age = ?, height = ?, body_weight = ?, goal = ?, gender = ?
                WHERE id = ?
            """, (age, height, weight, selected_goal, gender, profile["id"]))
            connection.commit()
            print("\n🔄 Profile successfully updated in database memory!")
        else:
            cursor.execute("""
                INSERT INTO user_profile (age, height, body_weight, goal, gender)
                VALUES (?, ?, ?, ?, ?)
            """, (age, height, weight, selected_goal, gender))
            connection.commit()
            print("\n Profile created successfully!")
            
        connection.close()
        return
        
    connection.close()



# ============================================================
# START WORKOUT MENU
# ============================================================

def start_workout_menu():

    while True:

        print("\n")
        print("##########################################")
        print("#              START WORKOUT             #")
        print("##########################################")

        print("\n1. Start today's workout")
        print("2. Add Workout")
        print("3. Exit")


        choice = input(
            "\nChoose option: "
        ).strip()


        # ----------------------------------------------------
        # START TODAY'S PLANNED WORKOUT
        # ----------------------------------------------------

        if choice == "1":

            start_todays_workout_plan()


        # ----------------------------------------------------
        # ADD WORKOUT WITHOUT FOLLOWING PLAN
        # ----------------------------------------------------

        elif choice == "2":

            add_workout()


        # ----------------------------------------------------
        # EXIT
        # ----------------------------------------------------

        elif choice == "3":

            break


        else:

            print(
                "\nInvalid option. "
                "Please choose 1, 2, or 3."
            )

# ============================================================
# PART 12A — BODY WEIGHT MENU
# ============================================================

def body_weight_menu():

    while True:

        print("\n")
        print("##########################################")
        print("#              BODY WEIGHT              #")
        print("##########################################")

        print("\n1. Record Body Weight")
        print("2. View Body Weight History")
        print("3. Delete Weight Entry")
        print("4. Back")


        choice = input(
            "\nChoose option: "
        ).strip()


        if choice == "1":

            record_body_weight()


        elif choice == "2":

            view_body_weight_history()


        elif choice == "3":

            delete_body_weight_entry()


        elif choice == "4":

            break


        else:

            print(
                "\nInvalid option."
            )
            
# ============================================================
# PART 12B — RECORD BODY WEIGHT
# ============================================================

def record_body_weight():

    print("\n")
    print("##########################################")
    print("#         RECORD BODY WEIGHT             #")
    print("##########################################")


    while True:

        weight_input = input(
            "\nEnter your body weight in kg: "
        ).strip()


        try:

            weight = float(weight_input)


            if weight <= 0:

                print(
                    "\nWeight must be greater than 0."
                )

                continue


            save_body_weight(weight)

            break


        except ValueError:

            print(
                "\nPlease enter a valid weight."
            )
# ============================================================
# PART 12C — DELETE BODY WEIGHT ENTRY
# ============================================================

def delete_body_weight_entry():

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()


    cursor.execute("""
        SELECT
            weight_id,
            weight,
            recorded_date,
            recorded_time

        FROM body_weight_history

        ORDER BY
            recorded_date DESC,
            recorded_time DESC
    """)


    records = cursor.fetchall()


    if not records:

        conn.close()

        print(
            "\nNo body weight records found."
        )

        return


    print("\n")
    print("##########################################")
    print("#       DELETE BODY WEIGHT ENTRY         #")
    print("##########################################")


    print("\nBody Weight History:")


    for number, record in enumerate(
        records,
        start=1
    ):

        weight_id, weight, date, time = record

        print(
            f"{number}. "
            f"{weight} kg — "
            f"{date} {time}"
        )


    print("\n0. Cancel")


    while True:

        try:

            choice = int(
                input(
                    "\nSelect entry to delete: "
                )
            )


            if choice == 0:

                conn.close()

                print(
                    "\nDeletion cancelled."
                )

                return


            if 1 <= choice <= len(records):

                selected = records[
                    choice - 1
                ]

                weight_id = selected[0]


                confirm = input(
                    "\nDelete this entry? "
                    "(yes/no): "
                ).lower().strip()


                if confirm == "yes":

                    cursor.execute("""
                        DELETE FROM body_weight_history

                        WHERE weight_id = ?
                    """, (weight_id,))


                    conn.commit()

                    print(
                        "\nBody weight entry "
                        "deleted successfully."
                    )

                else:

                    print(
                        "\nDeletion cancelled."
                    )


                conn.close()

                return


            print(
                "\nPlease select a valid entry."
            )


        except ValueError:

            print(
                "\nPlease enter a number."
            )
# ============================================================
# PART 13C — VIEW ALL WORKOUT HISTORY
# ============================================================

# ============================================================
# PART 14A — VIEW WORKOUT HISTORY
# ============================================================

def view_workout_history():

    connection = get_database_connection()
    cursor = connection.cursor()

    print("\n")
    print("##########################################")
    print("#          WORKOUT HISTORY              #")
    print("##########################################")

    cursor.execute("""
        SELECT
            id,
            day,
            workout_type,
            workout_date
        FROM workout_sessions
        ORDER BY workout_date DESC
    """)

    sessions = cursor.fetchall()

    if not sessions:

        print("\nNo workout history found.")

        connection.close()

        return


    for session in sessions:

        session_id = session[0]
        day = session[1]
        workout_type = session[2]
        workout_date = session[3]

        print("\n==========================================")

        print(
            f"Workout ID: {session_id}"
        )

        print(
            f"Date/Time: {workout_date}"
        )

        print(
            f"Day: {day}"
        )

        print(
            f"Type: {workout_type}"
        )

        print("==========================================")


        cursor.execute("""
            SELECT
                id,
                exercise_name
            FROM performed_exercises
            WHERE session_id = ?
            ORDER BY id
        """, (session_id,))

        exercises = cursor.fetchall()


        for exercise in exercises:

            performed_exercise_id = exercise[0]
            exercise_name = exercise[1]

            print(
                f"\nExercise: {exercise_name}"
            )


            cursor.execute("""
                SELECT
                    set_number,
                    reps,
                    weight
                FROM performed_sets
                WHERE performed_exercise_id = ?
                ORDER BY set_number
            """, (performed_exercise_id,))


            sets = cursor.fetchall()


            for workout_set in sets:

                set_number = workout_set[0]
                reps = workout_set[1]
                weight = workout_set[2]

                print(
                    f"  Set {set_number}: "
                    f"{reps} reps × "
                    f"{weight} kg"
                )


    connection.close()

# ============================================================
# PART 14B — DELETE WORKOUT HISTORY
# ============================================================

def delete_workout_history():

    connection = get_database_connection()
    cursor = connection.cursor()

    print("\n")
    print("##########################################")
    print("#         DELETE WORKOUT HISTORY        #")
    print("##########################################")


    # --------------------------------------------------------
    # GET ALL WORKOUT SESSIONS
    # --------------------------------------------------------

    cursor.execute("""
        SELECT
            id,
            day,
            workout_type,
            workout_date
        FROM workout_sessions
        ORDER BY workout_date DESC
    """)

    sessions = cursor.fetchall()


    if not sessions:

        print(
            "\nNo workout history found."
        )

        connection.close()

        return


    # --------------------------------------------------------
    # SHOW WORKOUTS
    # --------------------------------------------------------

    print("\nSaved Workouts:")

    for number, session in enumerate(
        sessions,
        start=1
    ):

        session_id = session[0]
        day = session[1]
        workout_type = session[2]
        workout_date = session[3]


        print(
            f"\n{number}. "
            f"{day} | "
            f"{workout_date} | "
            f"{workout_type}"
        )


    print(
        "\n0. Cancel"
    )


    # --------------------------------------------------------
    # SELECT WORKOUT
    # --------------------------------------------------------

    while True:

        try:

            choice = int(
                input(
                    "\nSelect workout to delete: "
                )
            )


            if choice == 0:

                print(
                    "\nDeletion cancelled."
                )

                connection.close()

                return


            if 1 <= choice <= len(sessions):

                break


            print(
                "\nPlease select a valid workout."
            )


        except ValueError:

            print(
                "\nPlease enter a number."
            )


    selected_session = sessions[
        choice - 1
    ]


    session_id = selected_session[0]


    # --------------------------------------------------------
    # CONFIRM DELETION
    # --------------------------------------------------------

    print("\n------------------------------------------")

    print(
        f"Selected workout:"
    )

    print(
        f"Date/Time: {selected_session[3]}"
    )

    print(
        f"Day: {selected_session[1]}"
    )

    print(
        f"Type: {selected_session[2]}"
    )

    print("------------------------------------------")


    confirm = input(
        "\nDelete this entire workout "
        "and all its sets? (yes/no): "
    ).lower().strip()


    if confirm != "yes":

        print(
            "\nDeletion cancelled."
        )

        connection.close()

        return


    # --------------------------------------------------------
    # GET PERFORMED EXERCISES
    # --------------------------------------------------------

    cursor.execute("""
        SELECT id
        FROM performed_exercises
        WHERE session_id = ?
    """, (session_id,))


    performed_exercises = cursor.fetchall()


    # --------------------------------------------------------
    # DELETE PERFORMED SETS
    # --------------------------------------------------------

    for performed_exercise in performed_exercises:

        performed_exercise_id = (
            performed_exercise[0]
        )


        cursor.execute("""
            DELETE FROM performed_sets
            WHERE performed_exercise_id = ?
        """, (performed_exercise_id,))


    # --------------------------------------------------------
    # DELETE PERFORMED EXERCISES
    # --------------------------------------------------------

    cursor.execute("""
        DELETE FROM performed_exercises
        WHERE session_id = ?
    """, (session_id,))


    # --------------------------------------------------------
    # DELETE WORKOUT SESSION
    # --------------------------------------------------------

    cursor.execute("""
        DELETE FROM workout_sessions
        WHERE id = ?
    """, (session_id,))


    # --------------------------------------------------------
    # SAVE DELETION
    # --------------------------------------------------------

    connection.commit()

    connection.close()


    print("\n==========================================")

    print(
        "Workout history deleted successfully."
    )

    print("==========================================")

# ============================================================
# PART 14C — WORKOUT HISTORY MENU
# ============================================================

def workout_history_menu():
    while True:
        print("\n")
        print("##########################################")
        print("#            WORKOUT HISTORY             #")
        print("##########################################")

        print("\n1. View All Workout History")
        print("2. View Today's Workouts")
        print("3. View This Week's Workouts")
        print("4. View This Month's Workouts")
        print("5. Delete Workout History")
        print("6. Back")

        choice = input("\nChoose option: ").strip()

        # ----------------------------------------------------
        # VIEW ALL
        # ----------------------------------------------------
        if choice == "1":
            view_workout_history()

        # ----------------------------------------------------
        # VIEW BY PERIODS
        # ----------------------------------------------------
        elif choice == "2":
            view_workout_history_by_period("today")

        elif choice == "3":
            view_workout_history_by_period("week")

        elif choice == "4":
            view_workout_history_by_period("month")

        # ----------------------------------------------------
        # DELETE
        # ----------------------------------------------------
        elif choice == "5":
            delete_workout_history()

        # ----------------------------------------------------
        # BACK
        # ----------------------------------------------------
        elif choice == "6":
            break

        else:
            print("\nInvalid option.")

# ============================================================
# PART 14D-1 — DATE-BASED WORKOUT HISTORY
# ============================================================

def view_workout_history_by_period(period):
    # Ensure correct datetime imports are active inside this scope to avoid crashes
    from datetime import datetime, timedelta

    connection = get_database_connection()
    cursor = connection.cursor()

    # --------------------------------------------------------
    # DETERMINE DATE RANGE
    # --------------------------------------------------------
    today = datetime.now().date()

    if period == "today":
        start_date = today
        end_date = today

    elif period == "week":
        start_date = today - timedelta(days=today.weekday())
        end_date = today

    elif period == "month":
        start_date = today.replace(day=1)
        end_date = today

    else:
        print("\nInvalid history period.")
        connection.close()
        return

    # --------------------------------------------------------
    # GET WORKOUT SESSIONS
    # --------------------------------------------------------
    cursor.execute("""
        SELECT id, day, workout_type, workout_date 
        FROM workout_sessions 
        WHERE DATE(workout_date) BETWEEN ? AND ? 
        ORDER BY workout_date DESC
    """, (start_date.isoformat(), end_date.isoformat()))

    sessions = cursor.fetchall()

    # --------------------------------------------------------
    # NO RESULTS
    # --------------------------------------------------------
    if not sessions:
        print("\n==========================================")
        if period == "today":
            print("NO WORKOUTS FOUND FOR TODAY")
        elif period == "week":
            print("NO WORKOUTS FOUND THIS WEEK")
        elif period == "month":
            print("NO WORKOUTS FOUND THIS MONTH")
        print("==========================================")
        connection.close()
        return

    # --------------------------------------------------------
    # DISPLAY TITLE
    # --------------------------------------------------------
    print("\n")
    print("==========================================")
    if period == "today":
        print("TODAY'S WORKOUTS")
    elif period == "week":
        print("THIS WEEK'S WORKOUTS")
    elif period == "month":
        print("THIS MONTH'S WORKOUTS")
    print("==========================================")

    # --------------------------------------------------------
    # DISPLAY SESSIONS
    # --------------------------------------------------------
    for session in sessions:
        session_id = session[0]
        day = session[1]
        workout_type = session[2]
        workout_date = session[3]

        print("\n------------------------------------------")
        print(f"Date/Time: {workout_date}")
        print(f"Day: {day}")
        print(f"Type: {workout_type}")
        print("------------------------------------------")

        # ----------------------------------------------------
        # GET EXERCISES
        # ----------------------------------------------------
        cursor.execute("""
            SELECT id, exercise_name 
            FROM performed_exercises 
            WHERE session_id = ? 
            ORDER BY id
        """, (session_id,))

        exercises = cursor.fetchall()

        for exercise in exercises:
            performed_exercise_id = exercise[0]
            exercise_name = exercise[1]

            print(f"\nExercise: {exercise_name}")

            # ------------------------------------------------
            # GET SETS
            # ------------------------------------------------
            cursor.execute("""
                SELECT set_number, reps, weight 
                FROM performed_sets 
                WHERE performed_exercise_id = ? 
                ORDER BY set_number
            """, (performed_exercise_id,))

            sets = cursor.fetchall()

            for workout_set in sets:
                set_number = workout_set[0]
                reps = workout_set[1]
                weight = workout_set[2]

                print(f"  Set {set_number}: {reps} reps × {weight} kg")

    connection.close()
# ============================================================
# PART 3B — LOGGED WORKOUT ANALYSER
# (Weekly reports, week/month comparisons, 3-month trend tracker)
# ============================================================

def get_week_bounds(reference_date=None, weeks_ago=0):
    """Returns (monday, sunday) date objects for the week containing
    reference_date (default today), shifted back by weeks_ago weeks."""
    if reference_date is None:
        reference_date = datetime.now().date()

    monday = reference_date - timedelta(days=reference_date.weekday())
    monday = monday - timedelta(weeks=weeks_ago)
    sunday = monday + timedelta(days=6)
    return monday, sunday



def get_weekly_summary_stats(start_date, end_date):
    """Returns workout count, distinct training days, total sets, total reps,
    and total volume for the given date range (used for the summary card)."""
    connection = get_database_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*), COUNT(DISTINCT date(workout_date))
        FROM workout_sessions
        WHERE date(workout_date) BETWEEN date(?) AND date(?)
    """, (start_date.isoformat(), end_date.isoformat()))
    workout_count, training_days = cursor.fetchone()

    cursor.execute("""
        SELECT COUNT(*), COALESCE(SUM(ps.reps), 0), COALESCE(SUM(ps.reps * ps.weight), 0)
        FROM performed_sets ps
        JOIN performed_exercises pe ON ps.performed_exercise_id = pe.id
        JOIN workout_sessions ws ON pe.session_id = ws.id
        WHERE date(ws.workout_date) BETWEEN date(?) AND date(?)
    """, (start_date.isoformat(), end_date.isoformat()))
    total_sets, total_reps, total_volume = cursor.fetchone()

    connection.close()

    return {
        "workouts": workout_count or 0,
        "training_days": training_days or 0,
        "sets": total_sets or 0,
        "reps": total_reps or 0,
        "volume": total_volume or 0.0
    }

def get_week_volume_change_pct(this_volume, prev_volume):
    """Returns the % change in total volume vs the previous week, or None
    if there's no prior-week data to compare against (same honesty rule
    used elsewhere: no fake 0% when there's simply nothing to compare)."""
    if prev_volume is None or prev_volume <= 0:
        return None
    return ((this_volume - prev_volume) / prev_volume) * 100


def generate_week_status_text(training_days, volume_change_pct):
    """Generates the short two-line status shown on the home-screen weekly
    card ('Consistent week' / 'Keep it up!' etc). Two independent signals:
    - training_days -> how many distinct days were trained this week,
      drives the headline (frequency/consistency).
    - volume_change_pct -> % change in total volume vs last week (or None
      if there's no prior week to compare), refines the subtext when
      available, otherwise falls back to a generic encouragement line.
    Pure function of numbers already returned elsewhere — no new
    database access, so it's cheap to call for any week."""

    if training_days <= 0:
        note = "No workouts logged"
        default_sub = "Let's get moving this week"
    elif training_days <= 2:
        note = "Getting started"
        default_sub = "Try adding another session or two"
    elif training_days <= 4:
        note = "Consistent week"
        default_sub = "Keep it up!"
    elif training_days <= 6:
        note = "Great consistency"
        default_sub = "Strong training frequency"
    else:
        note = "Excellent consistency"
        default_sub = "Outstanding dedication"

    if training_days <= 0:
        # No point commenting on volume trend if nothing was logged.
        return note, default_sub

    if volume_change_pct is None:
        sub_note = default_sub
    elif volume_change_pct >= 5:
        sub_note = "Volume trending up"
    elif volume_change_pct <= -15:
        sub_note = "Volume dropped noticeably"
    elif volume_change_pct <= -5:
        sub_note = "Slightly lower volume"
    else:
        sub_note = "Volume holding steady"

    return note, sub_note


def get_home_screen_week_summary(weeks_ago=0):
    """Single-call bundle for a FINALIZED home-screen weekly card (a week
    that has already ended). Do not use this for the current in-progress
    week — use get_in_progress_week_preview() for that instead, since a
    week isn't "final" until its Sunday has passed.
    weeks_ago=1 is last week, 2 is two weeks ago, etc.
    Returns this week's stats, the top-line volume % change vs the
    previous week (or None if there's no prior week to compare), and the
    generated status text. "workouts" (raw session count) is deliberately
    left out of the returned dict — it double-counts days with more than
    one logged session and reads as a confusing, redundant number next
    to training_days. training_days is the meaningful frequency metric."""
    this_monday, this_sunday = get_week_bounds(weeks_ago=weeks_ago)
    prev_monday, prev_sunday = get_week_bounds(weeks_ago=weeks_ago + 1)

    this_summary = get_weekly_summary_stats(this_monday, this_sunday)
    prev_summary = get_weekly_summary_stats(prev_monday, prev_sunday)

    has_prior_data = prev_summary["workouts"] > 0
    volume_change_pct = get_week_volume_change_pct(
        this_summary["volume"],
        prev_summary["volume"] if has_prior_data else None
    )

    note, sub_note = generate_week_status_text(
        this_summary["training_days"],
        volume_change_pct
    )

    return {
        "range_start": this_monday,
        "range_end": this_sunday,
        "training_days": this_summary["training_days"],
        "sets": this_summary["sets"],
        "reps": this_summary["reps"],
        "volume": this_summary["volume"],
        "volume_change_pct": volume_change_pct,  # None if no prior week
        "note": note,
        "sub_note": sub_note
    }


def get_in_progress_week_preview():
    """Minimal data for the CURRENT (still-running) week's locked/blurred
    home-screen card. Only training_days is meant to be visible through
    the lock — everything else (volume, sets, reps, note text, % change)
    stays hidden until the week ends and get_home_screen_week_summary()
    takes over on Monday. Deliberately returns nothing else, so there's
    no risk of the Flutter UI accidentally rendering a "final" number for
    a week that hasn't finished yet."""
    this_monday, this_sunday = get_week_bounds(weeks_ago=0)
    this_summary = get_weekly_summary_stats(this_monday, this_sunday)

    return {
        "range_start": this_monday,
        "range_end": this_sunday,
        "training_days": this_summary["training_days"]
    }


def get_block_overall_volume_stats(start_date, end_date):
    """
    Calculates total sets and absolute weight tonnage (Sets * Reps * Weight)
    accumulated inside the block boundaries to match Hevy-style macro analytics.
    """
    connection = get_database_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        SELECT COUNT(*), COALESCE(SUM(ps.reps * ps.weight), 0.0)
        FROM performed_sets ps
        JOIN performed_exercises pe ON ps.performed_exercise_id = pe.id
        JOIN workout_sessions ws ON pe.session_id = ws.id
        WHERE date(ws.workout_date) BETWEEN date(?) AND date(?)
    """, (start_date.isoformat(), end_date.isoformat()))
    
    total_sets, total_tonnage = cursor.fetchone()
    connection.close()
    return {"sets": total_sets or 0, "tonnage": total_tonnage or 0.0}

def get_weekly_effort_breakdown(start_date, end_date):
    """Returns {body_part: {'total_volume': float, 'total_sets': int,
    'not_defined_sets': int, 'high_effort_sets': int,
    'medium_effort_sets': int, 'low_effort_sets': int}} for every set
    logged in the period. total_volume stays raw weight×reps (unweighted
    by effort) — the effort breakdown is a separate, honestly-labeled
    quality view sitting alongside it, not merged into it."""
    connection = get_database_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT pe.exercise_id, ps.reps, ps.weight, ps.effort
        FROM performed_sets ps
        JOIN performed_exercises pe ON ps.performed_exercise_id = pe.id
        JOIN workout_sessions ws ON pe.session_id = ws.id
        WHERE date(ws.workout_date) BETWEEN date(?) AND date(?)
    """, (start_date.isoformat(), end_date.isoformat()))

    rows = cursor.fetchall()
    connection.close()

    body_part_data = {}

    for exercise_id, reps, weight, effort in rows:
        exercise = EXERCISES.get(exercise_id)
        if not exercise:
            continue

        for body_part in exercise["body_parts"]:
            if body_part not in body_part_data:
                body_part_data[body_part] = {
                    "total_volume": 0.0,
                    "total_sets": 0,
                    "not_defined_sets": 0,
                    "high_effort_sets": 0,
                    "medium_effort_sets": 0,
                    "low_effort_sets": 0,
                }

            data = body_part_data[body_part]
            data["total_volume"] += reps * weight
            data["total_sets"] += 1

            if effort is None:
                data["not_defined_sets"] += 1
            elif effort == "hard":
                data["high_effort_sets"] += 1
            elif effort == "medium":
                data["medium_effort_sets"] += 1
            elif effort == "easy":
                data["low_effort_sets"] += 1

    return body_part_data


def weekly_analysis_report(weeks_ago=0):
    """Prints the summary card + muscle breakdown for a given week.
    weeks_ago=0 is the current week, 1 is last week, 2 is two weeks ago, etc.
    Each week is always compared against the week immediately before it."""
    this_monday, this_sunday = get_week_bounds(weeks_ago=weeks_ago)
    prev_monday, prev_sunday = get_week_bounds(weeks_ago=weeks_ago + 1)

    this_summary = get_weekly_summary_stats(this_monday, this_sunday)
    this_breakdown = get_weekly_effort_breakdown(this_monday, this_sunday)
    prev_breakdown = get_weekly_effort_breakdown(prev_monday, prev_sunday)

    # Label matches how this week would read as a home-screen card
    if weeks_ago == 0:
        label = "THIS WEEK"
    elif weeks_ago == 1:
        label = "LAST WEEK"
    else:
        label = f"{weeks_ago} WEEKS AGO"

    # --- Summary card ---
    print("\n" + "=" * 45)
    print(f"{label} ({this_monday.strftime('%d %b')} - {this_sunday.strftime('%d %b')})")
    print("=" * 45)
    print(f"Workouts:       {this_summary['workouts']}")
    print(f"Training days:  {this_summary['training_days']}")
    print(f"Sets:           {this_summary['sets']}")
    print(f"Reps:           {this_summary['reps']}")
    print(f"Volume:         {this_summary['volume']:.1f} kg")
    print("=" * 45)

    # --- Per-muscle effort breakdown ---
    print("\nMuscle Group Breakdown:")
    print("-" * 45)

    if not this_breakdown:
        print("No workouts logged in this period.")
    else:
        # Same honesty rule as before: nothing logged last week at all
        # means there's no real baseline, not a fake 0% comparison.
        no_prior_week_data = not prev_breakdown

        for body_part in BODY_PARTS:
            data = this_breakdown.get(body_part)
            if data is None:
                continue  # not trained this week — skip rather than pad with zeros

            this_volume = data["total_volume"]

            if no_prior_week_data:
                volume_trend = "(no prior week to compare)"
            else:
                prev_volume = prev_breakdown.get(body_part, {}).get("total_volume", 0.0)
                if prev_volume > 0:
                    pct = ((this_volume / prev_volume) - 1) * 100
                    sign = "+" if pct >= 0 else ""
                    volume_trend = f"({sign}{pct:.1f}% vs last week)"
                elif this_volume > 0:
                    volume_trend = "(new this week)"
                else:
                    volume_trend = "(same as last week)"

            print(f"\n{body_part}")
            print(f"  Total volume: {this_volume:.1f}kg {volume_trend}")
            print(f"  Total sets performed: {data['total_sets']}")
            print(f"  Not defined sets: {data['not_defined_sets']}")
            print(f"  High effort sets: {data['high_effort_sets']}")
            print(f"  Medium effort sets: {data['medium_effort_sets']}")
            print(f"  Low effort sets: {data['low_effort_sets']}")

    print("\n" + "=" * 45)


def browse_weekly_cards():
    """CLI stand-in for the scrollable weekly-card UI: starts with the
    most recent 6 weeks, and lets you load further back on demand with
    no hard cutoff. Weeks with no logged activity still show up in the
    list (as a card reading zero), they are never silently skipped."""
    weeks_loaded = 6
    LOAD_BATCH_SIZE = 6

    while True:
        print("\n")
        print("##########################################")
        print("#      BROWSE WEEKLY CARDS               #")
        print("##########################################")

        for weeks_ago in range(weeks_loaded):
            if weeks_ago == 0:
                label = "This Week"
            elif weeks_ago == 1:
                label = "Last Week"
            else:
                label = f"{weeks_ago} Weeks Ago"
            print(f"{weeks_ago + 1}. {label}")

        load_more_option = weeks_loaded + 1
        back_option = weeks_loaded + 2

        print(f"{load_more_option}. Load {LOAD_BATCH_SIZE} More Weeks")
        print(f"{back_option}. Back to Analyser Menu")

        choice = input("\nChoose option: ").strip()

        if choice.isdigit() and 1 <= int(choice) <= weeks_loaded:
            weekly_analysis_report(weeks_ago=int(choice) - 1)
        elif choice == str(load_more_option):
            weeks_loaded += LOAD_BATCH_SIZE
        elif choice == str(back_option):
            return
        else:
            print(f"\nInvalid option. Please choose 1-{back_option}.")


# ============================================================
# PART 3C — 4-WEEK BLOCK ANALYSIS
# (Automatic mesocycle blocks, anchored to the user's first-ever
# logged workout. Two honest metrics per muscle group: Strength
# Trend (e1RM-based) and Effort Volume (effective-sets-based) —
# never merged into one fake composite number.)
# ============================================================

BLOCK_LENGTH_DAYS = 28
EFFECTIVE_REP_MIN = 5   # widened hypertrophy/strength working-set window
EFFECTIVE_REP_MAX = 20  # (see conversation: avoids excluding low-rep strength work)


def get_first_workout_date():
    """Returns the date of the user's earliest logged workout ever, or
    None if nothing has been logged yet. This is the fallback anchor —
    used directly only if no 'Starting Again' reset has ever happened."""
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT MIN(date(workout_date)) FROM workout_sessions")
    row = cursor.fetchone()
    connection.close()

    if row and row[0]:
        return datetime.strptime(row[0], "%Y-%m-%d").date()
    return None


def get_latest_reset_date():
    """Returns the date of the most recent 'Starting Again' reset, or
    None if the user has never reset. Multiple resets over time are
    supported — this always returns the latest one."""
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT MAX(reset_date) FROM training_resets")
    row = cursor.fetchone()
    connection.close()

    if row and row[0]:
        return datetime.strptime(row[0], "%Y-%m-%d").date()
    return None


def get_era_anchor_date():
    """The real anchor for everything block/progress-related: the most
    recent reset date if one exists, otherwise the very first-ever
    logged workout. Nothing before this date counts for blocks or for
    personal-best comparisons — but nothing is ever deleted, so older
    data stays available for future cross-era comparison features."""
    reset_date = get_latest_reset_date()
    if reset_date is not None:
        return reset_date
    return get_first_workout_date()


def get_block_bounds(blocks_ago=0):
    """Returns (start_date, end_date, total_completed_blocks) for a given
    block. blocks_ago=0 is the most recently COMPLETED block (not the
    in-progress one). Blocks are stored/derived chronologically from the
    current training era's anchor — nothing is renumbered when a new
    block completes, only the label shown to the user changes. A
    'Starting Again' reset shifts this anchor forward, giving the user
    a genuinely fresh Block 1 without touching any historical data."""
    anchor = get_era_anchor_date()
    if anchor is None:
        return None, None, 0

    today = datetime.now().date()
    elapsed_days = (today - anchor).days
    total_completed_blocks = elapsed_days // BLOCK_LENGTH_DAYS

    if total_completed_blocks == 0:
        return None, None, 0

    block_number = total_completed_blocks - blocks_ago  # 1-indexed, chronological
    if block_number < 1:
        return None, None, total_completed_blocks

    start = anchor + timedelta(days=(block_number - 1) * BLOCK_LENGTH_DAYS)
    end = start + timedelta(days=BLOCK_LENGTH_DAYS - 1)
    return start, end, total_completed_blocks


def get_block_raw_data(start_date, end_date):
    """Returns {exercise_id: {week_index(0-3): {'max_e1rm': float,
    'effective_sets': float}}} for every set logged inside the block.
    'effective_sets' is now effort-weighted (1.0 hard, 0.7 medium,
    0.0 easy, sub-5-rep sets always 0 here regardless of effort) rather
    than a binary rep-range count — falls back to the old 5-20 rep
    rule only when a set has no effort rating at all."""
    connection = get_database_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT pe.exercise_id, date(ws.workout_date), ps.reps, ps.weight, ps.effort
        FROM performed_sets ps
        JOIN performed_exercises pe ON ps.performed_exercise_id = pe.id
        JOIN workout_sessions ws ON pe.session_id = ws.id
        WHERE date(ws.workout_date) BETWEEN date(?) AND date(?)
    """, (start_date.isoformat(), end_date.isoformat()))

    rows = cursor.fetchall()
    connection.close()

    data = {}

    for exercise_id, workout_date_str, reps, weight, effort in rows:
        workout_date = datetime.strptime(workout_date_str, "%Y-%m-%d").date()
        week_index = (workout_date - start_date).days // 7
        week_index = max(0, min(3, week_index))  # clamp, just in case

        if exercise_id not in data:
            data[exercise_id] = {}
        if week_index not in data[exercise_id]:
            data[exercise_id][week_index] = {"max_e1rm": 0.0, "effective_sets": 0.0}

        # Epley's e1RM — no rep-range filter, matches daily-performance step
        e1rm = weight * (1 + (reps / 30))
        if e1rm > data[exercise_id][week_index]["max_e1rm"]:
            data[exercise_id][week_index]["max_e1rm"] = e1rm

        # Effort-weighted contribution toward volume
        data[exercise_id][week_index]["effective_sets"] += compute_effective_credit(reps, effort)

    return data


def compute_single_exercise_strength_trend(weeks_data):
    """The core per-exercise, WITHIN-block strength trend: first active
    week vs the rest of the block, e1RM-based. Returns None if there
    aren't enough repeats (< 2 active weeks) to mean anything. This is
    the exact same calculation compute_block_strength_trends averages
    across exercises to build each muscle group's Strength Trend — so
    an exercise's own number and its muscle's number are traceably the
    same math, not two unrelated ideas."""
    active_weeks = sorted(weeks_data.keys())
    active_count = len(active_weeks)

    if active_count < 2:
        return None

    first_active_week = active_weeks[0]
    baseline = weeks_data[first_active_week]["max_e1rm"]

    if baseline <= 0:
        return None

    actual_sum = sum(weeks_data[w]["max_e1rm"] for w in active_weeks)
    return ((actual_sum / (baseline * active_count)) - 1) * 100


def compute_block_strength_trends(raw_data):
    """Returns {body_part: pct_or_None}. Only exercises with >= 2 active
    weeks in the block count — anchored to the FIRST ACTIVE week for that
    exercise, not a hardcoded calendar week 1 (this is the fix for the
    case where someone skips a muscle group in the literal first week)."""
    per_body_part_progress = {}  # body_part -> list of valid exercise progress %

    for exercise_id, weeks in raw_data.items():
        exercise = EXERCISES.get(exercise_id)
        if not exercise:
            continue

        progress_pct = compute_single_exercise_strength_trend(weeks)
        if progress_pct is None:
            continue  # not enough repeating data — excluded, not faked

        for body_part in exercise["body_parts"]:
            per_body_part_progress.setdefault(body_part, []).append(progress_pct)

    result = {}
    for body_part in BODY_PARTS:
        values = per_body_part_progress.get(body_part)
        result[body_part] = (sum(values) / len(values)) if values else None
    return result


def compute_block_volume_trends(raw_data):
    """Returns {body_part: pct_or_None}. Counts EVERY exercise touching
    that muscle group, even if logged only once — unlike the strength
    metric, this one is meant to catch people who vary their exercises."""
    body_part_weekly_sets = {}  # body_part -> {week_index: total_effective_sets}

    for exercise_id, weeks in raw_data.items():
        exercise = EXERCISES.get(exercise_id)
        if not exercise:
            continue

        for body_part in exercise["body_parts"]:
            if body_part not in body_part_weekly_sets:
                body_part_weekly_sets[body_part] = {}
            for week_index, week_data in weeks.items():
                body_part_weekly_sets[body_part][week_index] = (
                    body_part_weekly_sets[body_part].get(week_index, 0)
                    + week_data["effective_sets"]
                )

    result = {}
    for body_part in BODY_PARTS:
        weekly_sets = body_part_weekly_sets.get(body_part)

        if not weekly_sets or sum(weekly_sets.values()) == 0:
            result[body_part] = None  # never trained this block — not "0% progress"
            continue

        active_weeks = sorted(weekly_sets.keys())
        active_count = len(active_weeks)
        first_active_week = active_weeks[0]
        baseline = weekly_sets[first_active_week]

        if baseline <= 0:
            result[body_part] = None  # no usable baseline
            continue

        actual_sum = sum(weekly_sets[w] for w in active_weeks)
        progress_pct = ((actual_sum / (baseline * active_count)) - 1) * 100
        result[body_part] = progress_pct

    return result

def get_blocks_before(block_start_date):
    """Returns [(start, end), ...] for every completed block strictly
    before block_start_date, within the current training era. Used to
    build the block-average baseline instead of a single all-time peak."""
    era_start = get_era_anchor_date()
    if era_start is None:
        return []

    this_block_number = ((block_start_date - era_start).days // BLOCK_LENGTH_DAYS) + 1
    blocks = []
    for block_number in range(1, this_block_number):
        s = era_start + timedelta(days=(block_number - 1) * BLOCK_LENGTH_DAYS)
        e = s + timedelta(days=BLOCK_LENGTH_DAYS - 1)
        blocks.append((s, e))
    return blocks


def get_exercise_average_before(exercise_id, block_start_date):
    """Average of this exercise's top weight and best e1RM across every
    PRIOR completed block in the current era (not a single all-time
    peak). This avoids a single unusually-good block making every
    later block look like a decline by comparison. Returns None if
    there's no prior block with data for this exercise yet."""
    prior_blocks = get_blocks_before(block_start_date)

    per_block_max_weights = []
    per_block_max_e1rms = []

    for block_start, block_end in prior_blocks:
        stats = get_exercise_block_stats(exercise_id, block_start, block_end)
        if stats is not None:
            per_block_max_weights.append(stats["max_weight"])
            per_block_max_e1rms.append(stats["max_e1rm"])

    if not per_block_max_weights:
        return None

    return {
        "avg_max_weight": sum(per_block_max_weights) / len(per_block_max_weights),
        "avg_max_e1rm": sum(per_block_max_e1rms) / len(per_block_max_e1rms),
        "blocks_counted": len(per_block_max_weights),
    }


def get_exercise_block_stats(exercise_id, start_date, end_date):
    """This block's numbers for one exercise: top weight, reps at that
    weight, best e1RM, this exercise's own volume trend, and its WITHIN
    this block strength trend (first active week vs the rest — the
    plateau-catcher, using the exact same math as the muscle-group
    Strength Trend, just for one exercise instead of averaged)."""
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT date(ws.workout_date), ps.reps, ps.weight, ps.effort
        FROM performed_sets ps
        JOIN performed_exercises pe ON ps.performed_exercise_id = pe.id
        JOIN workout_sessions ws ON pe.session_id = ws.id
        WHERE pe.exercise_id = ? AND date(ws.workout_date) BETWEEN date(?) AND date(?)
    """, (exercise_id, start_date.isoformat(), end_date.isoformat()))
    rows = cursor.fetchall()
    connection.close()

    if not rows:
        return None

    max_weight = max(r[2] for r in rows)
    reps_at_max_weight = max(r[1] for r in rows if r[2] == max_weight)
    max_e1rm = max(r[2] * (1 + (r[1] / 30)) for r in rows)

    weekly_effective_sets = {}
    weekly_e1rm_data = {}  # week_index -> {"max_e1rm": float}, for the within-block trend

    for date_str, reps, weight, effort in rows:
        workout_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        week_index = max(0, min(3, (workout_date - start_date).days // 7))

        credit = compute_effective_credit(reps, effort)
        weekly_effective_sets[week_index] = weekly_effective_sets.get(week_index, 0.0) + credit

        e1rm = weight * (1 + (reps / 30))
        if week_index not in weekly_e1rm_data:
            weekly_e1rm_data[week_index] = {"max_e1rm": 0.0}
        if e1rm > weekly_e1rm_data[week_index]["max_e1rm"]:
            weekly_e1rm_data[week_index]["max_e1rm"] = e1rm

    volume_pct = None
    if weekly_effective_sets:
        active_weeks = sorted(weekly_effective_sets.keys())
        active_count = len(active_weeks)
        first_active_week = active_weeks[0]
        baseline = weekly_effective_sets[first_active_week]
        if baseline > 0:
            actual_sum = sum(weekly_effective_sets[w] for w in active_weeks)
            volume_pct = ((actual_sum / (baseline * active_count)) - 1) * 100

    within_block_trend_pct = compute_single_exercise_strength_trend(weekly_e1rm_data)

    return {
        "max_weight": max_weight,
        "reps_at_max_weight": reps_at_max_weight,
        "max_e1rm": max_e1rm,
        "volume_pct": volume_pct,
        "within_block_trend_pct": within_block_trend_pct,
    }


def print_exercise_progress_card(exercise_id, start_date, end_date):
    exercise = EXERCISES.get(exercise_id)
    display_name = exercise["name"] if exercise else exercise_id

    prior = get_exercise_average_before(exercise_id, start_date)
    block_stats = get_exercise_block_stats(exercise_id, start_date, end_date)

    print("\n" + "=" * 55)
    print(f"{display_name.upper()} — PROGRESS")
    print("=" * 55)

    if block_stats is None:
        print("No sets logged for this exercise in this block.")
        print("=" * 55)
        return

    # 1. Weight vs the average of all prior blocks (not a single peak)
    if prior is None:
        print("1. First block tracking this exercise — no prior blocks to compare yet.")
    else:
        weight_diff = block_stats["max_weight"] - prior["avg_max_weight"]
        block_word = "block" if prior["blocks_counted"] == 1 else "blocks"
        baseline_note = f"(avg of last {prior['blocks_counted']} {block_word}: {prior['avg_max_weight']:.1f}kg)"
        if weight_diff > 0:
            print(f"1. ⬆️  {weight_diff:.1f}kg above your block average {baseline_note}")
        elif weight_diff < 0:
            print(f"1. ⬇️  {abs(weight_diff):.1f}kg below your block average {baseline_note}")
        else:
            print(f"1. Matches your block average exactly {baseline_note}")

    # 2. This block's top weight (plain PR for the block)
    print(f"2. This block's top weight: {block_stats['max_weight']:.1f}kg")

    # 3. Estimated 1RM (Epley, best set this block)
    print(f"3. Estimated 1-rep max this block: {block_stats['max_e1rm']:.1f}kg")

    # 4. WITHIN this block — did the exercise itself actually progress
    # week to week, independent of any other block? This is the
    # plateau-catcher, using the exact same math as the muscle-group
    # Strength Trend, just for this one exercise.
    within_pct = block_stats["within_block_trend_pct"]
    if within_pct is None:
        print("4. Within this block: N/A — not repeated enough weeks this")
        print("   block to measure week-to-week progression.")
    elif within_pct > 0:
        sign = "+"
        print(f"4. Within this block: {sign}{within_pct:.1f}% — trending up across the weeks.")
    elif within_pct < 0:
        print(f"4. Within this block: {within_pct:.1f}% — trending down across the weeks.")
    else:
        print("4. Within this block: 0.0% — flat, no weight/rep progression")
        print("   week to week. This exercise likely isn't driving further")
        print("   growth — consider adding weight or reps.")

    # 5. Volume trend for this exercise specifically
    if block_stats["volume_pct"] is None:
        print("5. Volume trend: N/A — no comparable baseline this block.")
    else:
        sign = "+" if block_stats["volume_pct"] >= 0 else ""
        print(f"5. Overall volume this block: {sign}{block_stats['volume_pct']:.1f}%")

    print("=" * 55)


def show_exercise_progress_menu(exercise_ids, start_date, end_date):
    """Lists every exercise trained in this block, lets the user pick
    one to see its full progress card, loops until they go back."""
    ordered_ids = sorted(
        exercise_ids,
        key=lambda eid: EXERCISES.get(eid, {}).get("name", eid)
    )

    while True:
        print("\n")
        print("##########################################")
        print("#        EXERCISE PROGRESS               #")
        print("##########################################")

        for idx, eid in enumerate(ordered_ids, start=1):
            name = EXERCISES.get(eid, {}).get("name", eid)
            print(f"{idx}. {name}")

        back_option = len(ordered_ids) + 1
        print(f"{back_option}. Back")

        choice = input("\nChoose exercise: ").strip()

        if choice == str(back_option):
            return
        elif choice.isdigit() and 1 <= int(choice) <= len(ordered_ids):
            selected_id = ordered_ids[int(choice) - 1]
            print_exercise_progress_card(selected_id, start_date, end_date)
            input("\nPress Enter to continue...")
        else:
            print(f"\nInvalid option. Please choose 1-{back_option}.")


def browse_block_history_menu():
    """
    Paged navigation loop matching the weekly card UI strategy.
    Always visible from Day 1 so users know the feature exists,
    using an engaging preview state for empty databases.
    """
    # 1. Fetch total completed blocks normally
    _, _, total_completed_blocks = get_block_bounds(blocks_ago=0)

    # Day One Safeguard: If they have 0 blocks, we force the list to show 1 preview block
    is_preview_mode = (total_completed_blocks == 0)
    blocks_to_display = 1 if is_preview_mode else min(6, total_completed_blocks)
    LOAD_BATCH_SIZE = 6

    while True:
        print("\n")
        print("##########################################")
        print("#      BROWSE COMPLETED BLOCKS MAP       #")
        print("##########################################")
        
        if is_preview_mode:
            print("Displaying: 1 Preview Block Available")
        else:
            print(f"Displaying {blocks_to_display} of {total_completed_blocks} completed blocks.")

        # Print the block rows
        for idx in range(blocks_to_display):
            if is_preview_mode:
                print(f"1. 🔒 Block 1 (Locked)    | [Complete your first 28 days to unlock]")
            else:
                start, end, _ = get_block_bounds(blocks_ago=idx)
                label = "Latest Completed Block" if idx == 0 else f"Block {total_completed_blocks - idx}"
                print(f"{idx + 1}. {label:<22} | [{start.strftime('%d %b')} - {end.strftime('%d %b')}]")

        # Dynamic structural menu routing keys
        load_more_option = blocks_to_display + 1
        back_option = blocks_to_display + 2

        print("-" * 42)
        if not is_preview_mode and blocks_to_display < total_completed_blocks:
            print(f"{load_more_option}. 🔄 Load {LOAD_BATCH_SIZE} More Completed Blocks")
        print(f"{back_option}. ↩️ Back to Analyser Menu")

        choice = input("\nChoose block option or number: ").strip()

        # Route 1: Back selection
        if choice == str(back_option):
            return

        # Route 2: Load Next Batch Selection
        elif not is_preview_mode and choice == str(load_more_option) and blocks_to_display < total_completed_blocks:
            blocks_to_display = min(blocks_to_display + LOAD_BATCH_SIZE, total_completed_blocks)
            continue

        # Route 3: Deep-Dive Selection for Day One Preview Mode
        elif choice == "1" and is_preview_mode:
            while True:
                print("\n============================================================")
                print("🔒  BLOCK 1 OPTIONS (PREVIEW MODE)")
                print("============================================================")
                print("1. View Muscle Group Summary Sheets (Strength & Volume Metrics)")
                print("2. 🔍 See Exercise Progress (PR Trends, 1RM & Rep Counts)")
                print("3. Back to Block List")
                
                sub_opt = input("\nChoose selection choice: ").strip()
                
                if sub_opt in ["1", "2"]:
                    print("\n============================================================")
                    print("🔒 FEATURE LOCKED")
                    print("============================================================")
                    print("Log your daily exercises in 'Start Workout' to build history.")
                    print("Once your first 28-day cycle completes, this dashboard will")
                    print("automatically activate your personal up/down progress arrows!")
                    print("============================================================")
                    input("\nPress Enter to return...")
                elif sub_opt == "3":
                    break

        # Route 4: Deep-Dive Selection for Active Users with Data
        elif choice.isdigit() and 1 <= int(choice) <= blocks_to_display and not is_preview_mode:
            selected_offset = int(choice) - 1
            start, end, _ = get_block_bounds(blocks_ago=selected_offset)
            raw_data = get_block_raw_data(start, end)
            
            while True:
                print("\n============================================================")
                print(f"📈 BLOCK {total_completed_blocks - selected_offset} REPORT OPTIONS")
                print("============================================================")
                print("1. View Muscle Group Summary Sheets (Strength & Volume)")
                print("2. 🔍 See Exercise Progress (PR Trends, 1RM & Rep Counts)")
                print("3. Back to Block List")
                
                sub_opt = input("\nChoose option: ").strip()
                
                if sub_opt == "1":
                    strength_trends = compute_block_strength_trends(raw_data)
                    volume_trends = compute_block_volume_trends(raw_data)
                    
                    # Fetch overall tonnage progress (Hevy feature matching)
                    current_stats = get_block_overall_volume_stats(start, end)
                    prev_start = start - timedelta(days=28)
                    prev_end = start - timedelta(days=1)
                    prior_stats = get_block_overall_volume_stats(prev_start, prev_end)
                    
                    print("\n" + "=" * 55)
                    print(f"📊  MACRO BLOCK PERFORMANCE REPORT (BLOCK {total_completed_blocks - selected_offset})")
                    print("=" * 55)
                    
                    if prior_stats["sets"] > 0 and prior_stats["tonnage"] > 0:
                        vol_pct_change = ((current_stats["tonnage"] - prior_stats["tonnage"]) / prior_stats["tonnage"]) * 100
                        sign = "+" if vol_pct_change >= 0 else ""
                        print(f"📌  OVERALL BLOCK VOLUME WORKLOAD : {sign}{vol_pct_change:.1f}% TOTAL TONNAGE EXP 🚀")
                        print(f"    Total Working Sets Logged     : {current_stats['sets']} Sets vs {prior_stats['sets']} Prior")
                        print(f"    Total Dynamic Tonnage Lifted  : {current_stats['tonnage']:.1f} kg vs {prior_stats['tonnage']:.1f} kg")
                    else:
                        print(f"📌  OVERALL BLOCK VOLUME WORKLOAD : {current_stats['sets']} Total Sets Logged (Baseline month)")
                        print(f"    Total Dynamic Tonnage Lifted  : {current_stats['tonnage']:.1f} kg")
                    print("-" * 55)

                    for body_part in BODY_PARTS:
                        st = strength_trends.get(body_part)
                        vt = volume_trends.get(body_part)
                        if st is None and vt is None: continue
                        print(f"\n💪 {body_part.upper()}")
                        print(f"  ⚡ Strength Trend: {f'+{st:.1f}%' if st and st>=0 else f'{st:.1f}%' if st else '--'}")
                        print(f"  📦 Effort Volume : {f'+{vt:.1f}%' if vt and vt>=0 else f'{vt:.1f}%' if vt else '--'}")
                    print("\n" + "=" * 55)
                    input("\nPress Enter to return...")
                    
                elif sub_opt == "2":
                    show_exercise_progress_menu(list(raw_data.keys()), start, end)
                elif sub_opt == "3":
                    break
        else:
            print(f"\nInvalid option. Select a number up to {back_option}")



def trigger_starting_again():
    """Global reset: records today as the start of a new training era.
    Nothing is deleted — every set ever logged stays in the database.
    From this point on, block numbering and 'personal best' comparisons
    only look at data from today forward, so a return from a long break
    isn't unfairly compared against an old peak."""
    print("\n" + "=" * 55)
    print("STARTING AGAIN")
    print("=" * 55)
    print("This resets your block count and personal-best comparisons")
    print("to start fresh from today. Nothing gets deleted — your full")
    print("history stays saved for future comparison features.")
    confirm = input("\nAre you starting again? (yes/no): ").strip().lower()

    if confirm != "yes":
        print("\nCancelled — nothing changed.")
        return

    today_str = datetime.now().date().isoformat()
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO training_resets (reset_date) VALUES (?)", (today_str,))
    connection.commit()
    connection.close()

    print(f"\nDone. Your new training era starts today ({today_str}).")
    print("Block 1 and fresh personal bests begin from here.")


def workout_analysis_menu():
    while True:
        print("\n")
        print("##########################################")
        print("#      WORKOUT LOG ANALYSER              #")
        print("##########################################")
        print("1. Browse Weekly Cards (last 6 weeks, load more)")
        print("2. 4-Week Block Analysis (latest completed block)")
        print("3. Starting Again (reset blocks & personal bests)")
        print("4. Back to Main Menu")

        choice = input("\nChoose option: ").strip()

        if choice == "1":
            browse_weekly_cards()
        elif choice == "2":
            browse_block_history_menu()
        elif choice == "3":
            trigger_starting_again()
        elif choice == "4":
            return
        else:
            print("\nInvalid option. Please choose 1-4.")




# PART 4 — MAIN WORKOUT PLAN BUILDER MENU
# ============================================================
def workout_plan_builder():

    print("\n")
    print("##########################################")
    print("#      WORKOUT PLAN BUILDER              #")
    print("##########################################")


    while True:
        print("\n==========================================")
        print("PLAN BUILDER MENU")
        print("==========================================")
        print("1. Select Day & Edit Routine")
        print("2. 📊 Run Scientific Volume Analysis")
        print("3. Back to Main Menu")

        choice = input("\nChoose option: ").strip()

        # Routes directly to your smart analysis hub function
        if choice == "2":
            analyze_planned_workout_routine()
            continue

        elif choice == "3":
        	return

        elif choice == "1":
            day = select_day()
            
            if day is None:
                continue

            if (day in WORKOUT_PLAN and WORKOUT_PLAN[day]["body_parts"]):
                manage_day(day)
            else:
                build_day(day)

            another_day = input("\nModify another day? (yes/no): ").lower().strip()
            if another_day != "yes":
                break
        else:
            print("\nInvalid option. Please choose 1, 2, or 3.")


    print("\n")
    print("##########################################")
    print("#      CURRENT WEEKLY PLAN               #")
    print("##########################################")

    for day in DAYS:
        show_day_plan(day)


#@@@@@@@@@@@@@@@@
         #MAIN MENUE
#@@@@@@@@@@@@@####


def main_menu():
    while True:
        print("\n")
        print("##########################################")
        print("#             FITNESS APP                #")
        print("##########################################")
        print("1. View/Update Weekly Plan")
        print("2. Start Workout")
        print("3. Setup/Edit User Profile")
        print("4. Body Weight")
        print("5. Workout History")
        print("6. Workout Log Analyser")
        print("7. Exit")
        
        choice = input("\nChoose option: ").strip()
        
        if choice == "1":
            workout_plan_builder()
        elif choice == "2":
            start_workout_menu()
        elif choice == "3":
            create_profile_interface()
        elif choice == "4":
            body_weight_menu()
        elif choice == "5":
        	workout_history_menu()
        elif choice == "6":
            workout_analysis_menu()
        elif choice == "7":
            print("\nExiting application. Keep crushing it!")
            break
        else:
            print("\nInvalid option. Please choose 1, 2, 3, 4, 5, 6 or 7.")



# ============================================================
# APPLICATION INITIALIZATION
# ============================================================

# ============================================================
# DATABASE INITIALIZATION
# ============================================================

initialize_database()
initialize_plan_database()
create_workout_history_tables()
create_body_weight_table()
load_workout_plan()
# ============================================================
# START APPLICATION
# ============================================================
# Only launch the interactive CLI when this file is run directly
# (e.g. `python back-up.py`). When imported by the API layer, the
# table setup above still runs, but the input()/print() CLI loop
# does not — importing this module must never block on input().
if __name__ == "__main__":
    main_menu()