import configparser

cfg = configparser.ConfigParser()
cfg.read('system.ini')


def get_property(section_val, key_val):
    """
    取得設定檔資訊
    Args:
        section_val 節
        key_val 參數
    Returns:    設定值
    """
    if section_val is not None and key_val is not None:
        try:
            return cfg.get(str(section_val), str(key_val))
        except Exception as e:
            return None
    else:
        return None
