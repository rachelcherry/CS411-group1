def get_playlist_by_temperature(temperature):
    temperature = float(temperature)

    playlists_by_temp_range = {
        (None, 0): '4QlvsJUNi8TLpRioInxzy4',  # cold weather vibes
        (0, 10): '35X4dJ2scfVZW6suaVmLww',    # cold weather jazz
        (10, 20): '67zFsE96Yi2MBNvnGJvEtw',   # it's chilly out
        (20, 30): '1TqcAFxTdnZMT2k4NaTsHp',   # warm weather vibes
        (30, None): '4PqZeksEzsgfMlKCxqXsqv',  # hot weather music
    }

    for (min_temp, max_temp), playlist_id in playlists_by_temp_range.items():
        if (min_temp is None or temperature > min_temp) and (max_temp is None or temperature <= max_temp):
            return playlist_id

    return '2utjwWZnVjfAv2Helpzz69'  # Default playlist if no range matches
