from match_singleton import MatchSingleton


def decrement_time(window):
    """
    每 1/3 秒减少 Match 的倒计时时间。
    """
    match = MatchSingleton.get_instance()
    time_parts = match.time.split(":")
    if len(time_parts) == 2:
        minutes, seconds = map(int, time_parts)
        total_seconds = minutes * 60 + seconds

        if total_seconds > 0:
            total_seconds -= 1

        minutes, seconds = divmod(total_seconds, 60)
        match.time = f"{minutes:02}:{seconds:02}"
        window.event_managers["bottom"].update.emit()
