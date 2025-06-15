import os
import pathlib
import random

class NotificationSound:
    """ Sound player for Windows. """

    def __init__(self, sound_path):
        file = open(self._path)
        if not file.buffer.readable():
            raise(NotificationSoundException(f"{sound_path} is not playable.", NotificationSoundException.CODE_UNPLAYABLE))
        readable_buffer = file.buffer.read()
        try:
            import winsound
            winsound.PlaySound(readable_buffer, 4)
        except ImportError:
            raise(NotificationSoundException("`winsound` library is unsupported."))

class NotificationSoundException(BaseException):
    CODE_DEFAULT = 400
    # Not playable.
    CODE_UNPLAYABLE = 401
    def __init__(self, error_message:str='', error_code:int=CODE_UNPLAYABLE):
        super().__init__(error_message)
        self.error_code = error_code

if __name__ == '__main__':
    root_path = pathlib.Path(__file__).parent
    sounds_path = root_path.joinpath('sounds')
    sounds = os.listdir(sounds_path)

    NotificationSound(sounds_path.joinpath(random.choice(sounds)))