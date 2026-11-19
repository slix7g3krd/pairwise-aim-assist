"""第 59 批：手柄右摇杆轻推，准星在三个敌人之间来回粘，松开后又甩过头：瞄准辅..."""


def in_fov(angle, fov):
    """视野筛选：目标相对准星的角度必须落在视野半角以内。"""
    return abs(angle) <= fov / 2.0


def sensitivity_norm(sensitivity, base):
    """灵敏度归一：把玩家灵敏度换算成相对基准灵敏度的倍率。"""
    if base == 0:
        raise ValueError("base sensitivity must be non-zero")
    return sensitivity / base


def switch_hysteresis(new_score, old_score, threshold):
    """切换滞后：新目标分数必须超过旧目标一个阈值才允许切换，避免抖动。"""
    return new_score > old_score + threshold


def occlusion_ok(visible):
    """遮挡剔除：只有可见（无遮挡）的目标才允许被吸附。"""
    return bool(visible)


_DEVICE_SCALES = {
    "gamepad": 1.0,
    "mouse": 0.0,
    "touch": 0.6,
}


def device_scale(device):
    """输入设备缩放：不同输入设备使用统一的辅助强度缩放表。"""
    return _DEVICE_SCALES.get(device, 1.0)


def lag_target(current, past):
    """延迟目标：网络延迟下使用延迟补偿后的历史位置，而不是当前帧残影。"""
    return past


def aspect_scale(width, height):
    """宽高比归一：用宽高比修正横向吸附范围，宽屏/超宽屏表现一致。"""
    if height == 0:
        raise ValueError("height must be non-zero")
    return width / height


def threat_priority(distance, threat):
    """威胁优先级：单位距离上的威胁度，威胁越高、距离越近优先级越高。"""
    if distance == 0:
        raise ValueError("distance must be non-zero")
    return threat / distance


def recoil_separate(assist, recoil):
    """后坐力分离：从辅助量中扣除垂直后坐力分量，避免压枪与辅助叠加打架。"""
    return assist - recoil


def release_on_death(alive):
    """死亡释放：目标死亡（alive 为 False）时应释放吸附状态。"""
    return not alive


def frame_independent(dt, base):
    """帧率无关：按帧时长缩放辅助量，低帧率不会吸得更狠。"""
    return dt * base


def soft_lock(a, b, alpha):
    """软锁定：在两个重叠目标之间按 alpha 插值，避免准星在两者之间跳变。"""
    return a + (b - a) * alpha


def return_smooth(current, target, alpha):
    """回正平滑：取消辅助后按 alpha 插值平滑回正，避免镜头突然弹开。"""
    return current + (target - current) * alpha
