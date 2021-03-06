from yapsy.IPlugin import IPlugin

class PluginDataManager():
    '''
    Just a central data manager for plugins that need to share a single
    entity. This primarily powers the Pi Sense Hat so the entity can be
    used by both a sensor plugin and a display plugin
    '''
    def __init__(self):
        self.__data = dict()

    def get_entity(self, key):
        if key in self.__data:
            return self.__data[key]

        return None

    def store_entity(self, key, value):
        if key in self.__data:
            raise Exception("Entity already exists")

        self.__data[key] = value

    def del_entity(self, key):
        if key in self.__data:
            del self.__data[key]


class IRepositoryPlugin(IPlugin):

    def prepare(self, config, data_manager):
        '''
        Activate the plugin. This should set up whatever callbacks
        and connections this plugin intends to have in addition to
        the two defined by stormberry's plugin API.
        '''
        self.config = config
        self.data_manager = data_manager
        return True

    def shutdown(self):
        '''
        Called on shutdown or to reinitialize. Expected to close
        all connections and files as needed for a clean shutdown.
        '''
        pass

    def store_reading(self, reading):
        '''
        Store a weather reading

        Returns:
            True (success) or False (fail)
        '''
        return True

    def get_health(self):
        '''
        Health check method. Returns True (healthy) or False (unhealth)
        '''
        return True

    def get_latest(self):
        '''
        Gets the most recent reading from the data
        source.

        @return dict
        '''
        return None

    def get_between(self, start_time, end_time = None):
        '''
        Gets the weather readings between a start and
        optional end time. If end time is omitted,
        the end_time will be the most recent reading.

        @param start_time string
        @param end_time string
        @return []
        '''
        return []

    def get_mean_between(self, start_time, end_time = None):
        '''
        Gets the means for the readings between a start
        and optional end time. If end time is omitted,
        the end_time will be the most recent reading.

        @param start_time string
        @param end_time string
        @return []
        '''
        return []

    def get_extremes_between(self, start_time, end_time = None):
        '''
        Gets the means for the readings between a start
        and optional end time. If end time is omitted,
        the end_time will be the most recent reading.

        @param start_time string
        @param end_time string
        @return []
        '''
        return []


class ISensorPlugin(IPlugin):

    def prepare(self, config, data_manager):
        '''
        Activate the plugin. This should set up whatever callbacks
        and connections this plugin intends to have in addition to
        the two defined by stormberry's plugin API.
        '''
        self.config = config
        self.data_manager = data_manager
        return True

    def shutdown(self):
        '''
        Called on shutdown or to reinitialize. Expected to close
        all connections and files as needed for a clean shutdown.
        '''
        pass

    def in_operating_range(self, weather_reading):
        '''
        Whether we're outside the operating or accuracy range
        of the sensor. By default this returns True.

        This method recives the _previous_ weather reading
        the station has available. If this method returns
        False, the sensor will not be read by the station.
        '''
        return True

    def get_reading(self):
        '''
        Assemble and return a weather reading

        Returns:
            WeatherReading or None
        '''
        return None

    def get_health(self):
        '''
        Health check method. Returns True (healthy) or False (unhealth)
        '''
        return True


class IDisplayPlugin(IPlugin):
    '''
    A very basic display plugin for handling complex display needs. This is largely
    identical to the repository plugin but does not allow reading weather data.
    '''

    def prepare(self, config, data_manager):
        self.config = config
        self.data_manager = data_manager
        return True

    def shutdown(self):
        pass

    def update(self, weather_reading):
        return True

