class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        '''
        Method to Initialize TV Object
        '''
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
        

    def power(self):
        '''
        Method to mute television
        '''
        if self.__status == False:
            self.__status: bool = True
        else:
            self.__status: bool = False

    def mute(self):
        '''
        Method to mute television
        '''
        if self.__status:
            if self.__muted == True:
                self.__muted: bool = False
            else:
                self.__muted: bool = True

    def channel_up(self):
        '''
        Method to change channel upwards.
        '''
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            elif self.__channel >= Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        '''
        Method to change channel downwards.
        '''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            elif self.__channel <= Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        '''
        Method to turn down tv volume.
        '''
        if self.__status:
            self.__muted: bool = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        '''
        Method to turn up tv volume.
        '''
        if self.__status:
            self.__muted: bool = False
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
