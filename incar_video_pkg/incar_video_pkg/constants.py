'''This module houses the constants for scripts package in simulation application'''
from enum import Enum
import cv2

MAIN_CAMERA_TOPIC="/video_mjpeg"
VIDEO_STATE_SRV="/media_state"
IMU_TOPIC="/imu_msg/raw"
PUBLISH_SENSOR_TOPIC="/video/sensor_stream"
PUBLISH_VIDEO_TOPIC="/video/mp4_stream"


class RaceType(Enum):
    '''Enum containing the keys for race type
    '''
    TIME_TRIAL = "TIME_TRIAL"
    OBJECT_AVOIDANCE = "OBJECT_AVOIDANCE"
    HEAD_TO_BOT = "HEAD_TO_BOT"
    HEAD_TO_MODEL = "HEAD_TO_MODEL"
    F1 = "F1"
    LIVE = "LIVE"

class CameraTypeParams(Enum):
    """ This Enum contains the all the params for each camera topics
    Extends:
        Enum
    Variables:
        PIP_PARAMS (dict): picture in picture related information
        MAIN_CAMERA_PARAMS (dict): Main camera i.e, the camera view following the car
        SUB_CAMERA_PARAMS (dict): Sub camera i.e, the top view of the track
    """
    CAMERA_PIP_PARAMS = "camera_pip_params"
    CAMERA_45DEGREE_PARAMS = "camera_45degree_params"
    CAMERA_TOPVIEW_PARAMS = "camera_topview_params"
    CAMERA_FORWARD_PARAMS = "camera_forward_params"


class Mp4Parameter(Enum):
    """
    Describes the parameters used to save Mp4
    Extends:
        Enum
    """
    FOURCC = cv2.VideoWriter_fourcc(*'mp4v')
    FPS = 15
    FRAME_SIZE = (640, 480)


class RaceCarColorToRGB(Enum):
    """ Color to RGB mapping
    Extends:
        Enum
    """
    Black = (26, 26, 26)
    Grey = (135, 149, 150)
    Blue = (68, 95, 229)
    Red = (224, 26, 37)
    Orange = (255, 160, 10)
    White = (255, 255, 255)
    Purple = (159, 42, 195)


# Amount of time (in seconds) to wait, in order to prevent model state from
# spamming logs while the model is loading
WAIT_TO_PREVENT_SPAM = 2

# Radius of the circle plotted on the agent in pixels
RACECAR_CIRCLE_RADIUS = 30

# AWS Deepracer watermark
AWS_DEEPRACER_WATER_MARK = "AWS DeepRacer"

# Mapping the racetype to the text shown on the video
RACE_TYPE_TO_VIDEO_TEXT_MAPPING = {
    RaceType.TIME_TRIAL.value: "Time trial",
    RaceType.OBJECT_AVOIDANCE.value: "Object avoidance",
    RaceType.HEAD_TO_BOT.value: "Head-to-bot",
    RaceType.HEAD_TO_MODEL.value: "Head-to-head",
    RaceType.F1.value: "F1",
    RaceType.LIVE.value: "In-Car Live"
}

# Decrease the minor image by a scale of provided number
SCALE_RATIO = 2.5


# Image size
class IconographicImageSize(Enum):
    """ The images that are provided are not accurate.
    Also some of the image pixels requires even number for the math.

    Attributes:
        FULL_IMAGE_SIZE: This is the same size that is given out by camera
        BOT_CAR_IMAGE_SIZE: Making the size rectangular and even pixel. Enlarging it.
        OBSTACLE_IMAGE_SIZE: [description]
        AGENTS_IMAGE_SIZE: [description]
        RACE_COMPLETE_IMAGE_SIZE: [description]
    """
    FULL_IMAGE_SIZE = (640, 480)
    BOT_CAR_IMAGE_SIZE = (int(34//SCALE_RATIO), int(34//SCALE_RATIO))
    OBSTACLE_IMAGE_SIZE = (int(34//SCALE_RATIO), int(34//SCALE_RATIO))
    AGENTS_IMAGE_SIZE = (int(88//SCALE_RATIO), int(88//SCALE_RATIO))
    VIRTUAL_EVENT_AGENTS_IMAGE_SIZE = (int(66 // SCALE_RATIO), int(66 // SCALE_RATIO))
    RACE_COMPLETE_IMAGE_SIZE = (308, 40)


# Track iconography png enums
class TrackAssetsIconographicPngs(Enum):
    """ Track images enum mapping

    Attributes:
        AGENTS_PNG: Different agents color images
        BOTS_PNG: Image of the bot shown in graphinology
        OBSTACLES_PNG: Image of the obstacle shown in graphinology
        OBSTACLE_OVERLAY_PNG: Gradient for the obstacle
        HEAD_TO_HEAD_OVERLAY_PNG: Gradient for the head to head
        RACE_COMPLETE_OVERLAY_PNG: Shown when the race is complete
    """
    AGENTS_PNG = ["DRL_video_racer1", "DRL_video_racer2"]
    VIRTUAL_EVENT_AGENTS_PNG = ["virtual_event_racer1", "virtual_event_racer2"]
    BOTS_PNG = "DRL_video_bot"
    OBSTACLES_PNG = "DRL_video_obstacles"
    OBSTACLE_OVERLAY_PNG = "DRL_video_oa_overlay"
    HEAD_TO_HEAD_OVERLAY_PNG = "DRL_video_h2h_overlay"
    RACE_COMPLETE_OVERLAY_PNG = "DRL_video_racecomplete_overlay"
    HEAD_TO_HEAD_OVERLAY_PNG_LEAGUE_LEADERBOARD = "DRL_video_h2h_overlay_league_leaderboard"
    OBSTACLE_OVERLAY_PNG_LEAGUE_LEADERBOARD = "DRL_video_oa_overlay_league_leaderboard"
    #F1
    F1_LOGO_PNG = "F1_logo_official"
    F1_OVERLAY_DEFAULT_PNG = "F1_video_overlay_default"
    F1_OVERLAY_MIDWAY_PNG = "F1_video_overlay_midway"
    F1_OVERLAY_FINISHERS_PNG = "F1_video_overlay_finishers"
    F1_OVERLAY_TOPVIEW_2BOX_PNG = "F1_video_overlay_topview_2box"
    F1_OVERLAY_TOPVIEW_3BOX_PNG = "F1_video_overlay_topview_3box"
    F1_AGENTS_PNG = "./oval/oval"
    F1_AGENTS_NUM_PNG = "./numbers/number"
    F1_AGENTS_SLASH_DISPLAY_ICON_PNG = "./slash/slash"
    F1_AGENTS_RECT_DISPLAY_ICON_PNG = "./rectangle/rectangle"


# virtual event png
class VirtualEventIconographicPngs(Enum):
    OVERLAY_PNG = "virtual_event_overlay"
    SET = "virtual_event_set"
    GO = "virtual_event_go"
    FINISH = "virtual_event_finish"
    FINAL_FADING_IMAGE_50ALPHA = "final_fading_image_50alpha"


class TrackColors(Enum):
    """track sector colors
    """
    YELLOW = 'yellow'
    GREEN = 'green'
    PURPLE = 'purple'


class TrackSectorColors(Enum):
    """ track sector names and colors permutation
    """
    SECTOR1_YELLOW = 'sector1_yellow'
    SECTOR1_GREEN = 'sector1_green'
    SECTOR1_PURPLE = 'sector1_purple'
    SECTOR2_YELLOW = 'sector2_yellow'
    SECTOR2_GREEN = 'sector2_green'
    SECTOR2_PURPLE = 'sector2_purple'
    SECTOR3_YELLOW = 'sector3_yellow'
    SECTOR3_GREEN = 'sector3_green'
    SECTOR3_PURPLE = 'sector3_purple'


SECTOR_COLORS_DICT = \
    {TrackSectorColors.SECTOR1_YELLOW.value: "_virtual_event/track_layer_01_yellow",
     TrackSectorColors.SECTOR1_GREEN.value: "_virtual_event/track_layer_01_green",
     TrackSectorColors.SECTOR1_PURPLE.value: "_virtual_event/track_layer_01_purple",
     TrackSectorColors.SECTOR2_YELLOW.value: "_virtual_event/track_layer_02_yellow",
     TrackSectorColors.SECTOR2_GREEN.value: "_virtual_event/track_layer_02_green",
     TrackSectorColors.SECTOR2_PURPLE.value: "_virtual_event/track_layer_02_purple",
     TrackSectorColors.SECTOR3_YELLOW.value: "_virtual_event/track_layer_03_yellow",
     TrackSectorColors.SECTOR3_GREEN.value: "_virtual_event/track_layer_03_green",
     TrackSectorColors.SECTOR3_PURPLE.value: "_virtual_event/track_layer_03_purple"}


class VirtualEventMP4Params(Enum):
    """virtual event info dict for image editing state machine
    """
    IS_LEAGUE = 'is_league_leaderboard'
    COUNTDOWN_TIMER = 'countdown_timer'
    MAJOR_CV_IMAGE = 'major_cv_image'
    DISPLAY_NAME = 'display_name'
    CURRENT_LAP = 'current_lap'
    TOTAL_EVAL_SECONDS = 'total_eval_milli_seconds'
    RESET_COUNTER = 'reset_counter'
    SPEED = 'speed'
    CURR_PROGRESS = 'current_progress'
    LAST_EVAL_SECONDS = 'last_eval_time'
    X_MIN = 'x_min'
    X_MAX = 'x_max'
    Y_MIN = 'y_min'
    Y_MAX = 'y_max'
    SECTOR_TIMES = 'sector_times'
    BEST_LAP_TIME = 'best_lap_time'
    CURR_LAP_TIME = 'curr_lap_time'
    SECTOR_IMAGES = 'sector_images'
    FADER_OBJ = 'fader_obj'


class XYPixelLoc(Enum):
    """ The mp4 image size is (480, 640). Rendering text at different locations
    """
    MULTI_AGENT_DISPLAY_NAME_LOC = [(10, 10), (450, 10)]
    MULTI_AGENT_EVAL_TIME = (240, 10)
    SINGLE_AGENT_DISPLAY_NAME_LOC = (10, 10)
    SPEED_LEADERBOARD_LOC = (10, 410)
    SPEED_EVAL_LOC = (10, 420)
    LEADERBOARD_NAME_LOC = (10, 435)
    RACE_TYPE_EVAL_LOC = (10, 445)
    RACE_TYPE_RACE_LOC = (10, 455)
    AWS_DEEPRACER_WATER_MARK_LOC = (445, 450)
    TRAINING_PHASE_LOC = (40, 400)
    TRACK_IMG_WITH_OFFSET_LOC = (0, 20)
    TRACK_IMG_WITHOUT_OFFSET_LOC = (0, 0)


class VirtualEventXYPixelLoc(Enum):
    TRACK_IMG_VIRTUAL_EVENT_LOC = (0, 0)
    ICON = (30, 452)
    TIME_REMAINING_DIGIT = (60, 425)
    TIME_REMAINING_TEXT = (60, 460)
    SPEED_DIGIT = (220, 425)
    SPEED_TEXT = (220, 460)
    RESET_DIGIT = (350, 425)
    RESET_TEXT = (350, 460)
    CURRENT_LAP_TIME_DIGIT = (480, 425)
    CURRENT_LAP_TIME_TEXT = (480, 460)
    BEST_LAP_TIME_DIGIT = (480, 10)
    BEST_LAP_TIME_TEXT = (480, 45)


# Race completion flag y-offset
RACE_COMPLETE_Y_OFFSET = 180


# Mapping the racetype to the text shown on the video
class FrameQueueData(Enum):
    """ Enum for frame data put into the queue
    """
    FRAME = "frame",
    AGENT_METRIC_INFO = "agent_metric_info",
    TRAINING_PHASE = "training_phase"


# Agent Video editor constants
MAX_FRAMES_IN_QUEUE = 1500
KVS_PUBLISH_PERIOD = 1.0/15.0
QUEUE_WAIT_TIME = 10 # In seconds

# virtual event prepare digit font
VIRTUAL_EVENT_PREPARE_DIGIT_FONT = 100


class ModelImgNames(Enum):
    """ Mapping the different objects and agents image

    Attributes:
        OBJECT_IMGS: This could be boxes or the bots
        AGENT_IMGS: This is the agents image
        AGENT_NUM_IMGS: This is the agent number, used only in F1
    """
    OBJECT_IMGS = "object_imgs"
    AGENT_IMGS = "agent_imgs"
    AGENT_NUM_IMGS = "agent_num_imgs"


class FrameTypes(Enum):
    """ Different frames to be edited as part of Mp4 and KVS

    Attributes:
        MAIN_CAMERA_FRAME: Frames coming from 45degree camera
        TOP_CAMERA_FRAME: Frames from the top view camera
    """
    MAIN_CAMERA_FRAME = "main_camera_frame"
    TOP_CAMERA_FRAME = "top_camera_frame"


# Fader constants
class VirtualEventFader(Enum):
    """ These constants are used for virtual event fader class

    Attributes:
        FADING_MIN_PERCENT (float): Starting multiplier to gradient alpha value.
        FADING_MAX_PERCENT (float): Ending multiplier to gradient alpha value
        NUM_FRAMES (int): Number of frames the fading transitions occur.30 Frames = 2seconds if 15 FPS
    """
    FADING_MIN_PERCENT = 0
    FADING_MAX_PERCENT = 0.75
    NUM_FRAMES = 75
