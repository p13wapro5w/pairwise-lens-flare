"""第 55 批：镜头对着太阳时鬼影乱跳、遮挡物边缘漏光、HDR ..."""

def project_light(position, viewport):
    """把光源位置投影到屏幕坐标。"""
    raise NotImplementedError("TODO: project_light")

def occlusion_count(samples):
    """返回多点遮挡下的可见采样数。"""
    raise NotImplementedError("TODO: occlusion_count")

def ghost_count(aperture):
    """按光圈返回鬼影数量。"""
    raise NotImplementedError("TODO: ghost_count")

def flare_intensity(aperture, base):
    """按光圈返回耀斑强度。"""
    raise NotImplementedError("TODO: flare_intensity")

def highlight_threshold(value, threshold):
    """裁掉低于阈值的高光。"""
    raise NotImplementedError("TODO: highlight_threshold")

def transmission(alpha):
    """返回透明遮挡物透射率。"""
    raise NotImplementedError("TODO: transmission")

def update_fov(fov):
    """返回视野变化后的耀斑参数。"""
    raise NotImplementedError("TODO: update_fov")

def normalize_flares(values):
    """归一化多光源耀斑能量。"""
    raise NotImplementedError("TODO: normalize_flares")

def exclude_ui(is_ui):
    """判断耀斑是否排除 UI。"""
    raise NotImplementedError("TODO: exclude_ui")

def stereo_shift(view_id):
    """按眼别偏移耀斑位置。"""
    raise NotImplementedError("TODO: stereo_shift")
