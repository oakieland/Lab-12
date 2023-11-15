class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        '''
        Method to mute television
        :return: mute
        '''
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self):
        '''
        Method to mute television
        :return: mute
        '''
        if self.__status:
            if self.__muted == True:
                self.__muted = False
            else:
                self.__muted = False

    def channel_up(self):
        '''
        Method to change channel upwards.
        :return: tv channel
        '''
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
        elif self.__channel >= Television.MAX_CHANNEL:
            self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        '''
        Method to change channel downwards.
        :return: tv channel
        '''

        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            elif self.__channel <= Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        '''
        Method to turn down tv volume.
        :return: tv volume
        '''
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        '''
        Method to turn up tv volume.
        :return: tv volume
        '''
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        '''
        Method to show the tv status.
        :return: tv status
        '''
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'