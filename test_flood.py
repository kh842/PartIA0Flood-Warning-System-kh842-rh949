from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

def test_stations_level_over_threshold():
    s_id = "test-s-id1"
    m_id = "test-m-id1"
    label = "some station1"
    coord = (-2.0, 4.0)
    trange = (1, 2)
    river = "River X"
    town = "My Town1"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s1.latest_level = 1.5

    s_id = "test-s-id2"
    m_id = "test-m-id2"
    label = "some station2"
    coord = (-2.0, 4.0)
    trange = (2, 4)
    river = "River Y"
    town = "My Town2"
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s2.latest_level = 8

    s_id = "test-s-id3"
    m_id = "test-m-id3"
    label = "some station3"
    coord = (-2.0, 4.0)
    trange = (0, 2)
    river = "River Z"
    town = "My Town3"
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s3.latest_level = 4

    stations = [s1, s2, s3]
    thresh = stations_level_over_threshold(stations, 1.5)
    assert thresh == [(s2, s2.relative_water_level()), (s3, s3.relative_water_level())]


def test_stations_highest_rel_level():
    s_id = "test-s-id1"
    m_id = "test-m-id1"
    label = "some station1"
    coord = (-2.0, 4.0)
    trange = (1, 2)
    river = "River X"
    town = "My Town1"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s1.latest_level = 1.5

    s_id = "test-s-id2"
    m_id = "test-m-id2"
    label = "some station2"
    coord = (-2.0, 4.0)
    trange = (2, 4)
    river = "River Y"
    town = "My Town2"
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s2.latest_level = 8

    s_id = "test-s-id3"
    m_id = "test-m-id3"
    label = "some station3"
    coord = (-2.0, 4.0)
    trange = (0, 2)
    river = "River Z"
    town = "My Town3"
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s3.latest_level = 4

    stations = [s1, s2, s3]
    thresh = stations_highest_rel_level(stations, 2)
    assert thresh == [(s2, s2.relative_water_level()), (s3, s3.relative_water_level())]
