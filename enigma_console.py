from typing import List, Tuple, Union
import pickle
import os.path


class Rotor():
    '''Класс, представляющий ротор энигмы. Конструктор принимает два списка: список букв алфавита в алфавитном порядке
    и список букв в произвольном порядке'''

    def __init__(self, alph: List[str], rnd_alph: List[str]):
        self.alph = alph
        self.rnd_alph = rnd_alph

    def Schr(self, chr: str, shift: int, alpha: List[str]):
        '''Осуществляет шифр Цезаря. Принимает символ chr и сдвиг shift. Если символ имеет номер n в алфавитном массиве, вернется
        символ с номером n + shift. Массив закольцован, величина сдвига не должна первышать длину алфавита'''
        n = len(alpha)
        try:
            if chr in alpha:
                if shift + alpha.index(chr) > n - 1:
                    return alpha[shift + alpha.index(chr) - n]
                elif shift + alpha.index(chr) < 0:
                    return alpha[shift + alpha.index(chr) + n]
                else:
                    return alpha[shift + alpha.index(chr)]
            else:
                return chr
        except IndexError:
            print('Величина сдвига не должна первышать количество символов в алфавите')

    def ch_crpt(self, ch: str, shift: int):
        '''Возвращает элемент с тем же номером, из массива случайных символов, что имел символ, который вернула Schr'''
        ch_1 = self.Schr(ch, shift, self.alph)
        return self.rnd_alph[self.alph.index(ch_1)]

    def ch_crpt_rev(self, ch: str, shift: int):
        '''Возвращает элемент массива alph, с номером, соответсвующим номеру символа в rnd_alph, который соответсвует
        номеру символа ch + shift в alph. '''
        n = len(self.alph)
        ch_1i = self.alph.index(ch) + shift
        if ch_1i > n - 1:
            ch_1i = ch_1i - n
        elif ch_1i < 0:
            ch_1i = ch_1i + n
        ch_1 = self.alph[ch_1i]
        ch_2i = self.rnd_alph.index(ch_1)
        return self.alph[ch_2i]


# ---------------------------------------------------------------------------------------------------------------------

# массив alph и массивы rnd_alph
lang = (list('abcdefghijklmnopqrstuvwxyz'), list('абвгдеёжзийклмнопрстуфхцчщъыьэюя'))
eng = list('abcdefghijklmnopqrstuvwxyz')
rus = list('абвгдеёжзийклмнопрстуфхцчщъыьэюя')
rnd_eng_list = [list('ekmflgdqvzntowyhxuspaibrcj'),
                list('ajdksiruxblhwtmcqgznpyfvoe'),
                list('bdfhjlcprtxvznyeiwgakmusqo'),
                list('zygovxmhcjrpuktbwsieqnfadl'),
                list('hfagdyrnjmvqkbzextuopwicsl'),
                list('hfagdyrnjmvqkbzextuopwicsl'),
                list('hfagdyrnjmvqkbzextuopwicsl'), ]
#rnd_rus_list = [list("уюнвыхрчзсёълкпщаждэояиьгцмбйефт"),
#                list("ыфвоуэжюяхйеёдзанбилпьгмтцсщчърк"),
#                list("оюркнтдпфэчейжсиьбёхмцгъзущлыавя"),
#                list("юнрбэоьгчмипеёдщвсзтжцыяъхаклуфй"),
#                list("чнпауэцкмейьгизборфлсжёювъхядщыт"),
#                list("чжъиздпюутьнхбрфкгцаломщяыеёвэсй"),
#                list("мюгыхнаутрифжъяёлоэчщьзйцвпкесдб")]
lists = [[list('ekmflgdqvzntowyhxuspaibrcj'),
          list('ajdksiruxblhwtmcqgznpyfvoe'),
          list('bdfhjlcprtxvznyeiwgakmusqo'),
          list('zygovxmhcjrpuktbwsieqnfadl'),
          list('hfagdyrnjmvqkbzextuopwicsl'),
          list('hfagdyrnjmvqkbzextuopwicsl'),
          list('hfagdyrnjmvqkbzextuopwicsl'), ], [list("уюнвыхрчзсёълкпщаждэояиьгцмбйефт"),
                                                  list("ыфвоуэжюяхйеёдзанбилпьгмтцсщчърк"),
                                                  list("оюркнтдпфэчейжсиьбёхмцгъзущлыавя"),
                                                  list("юнрбэоьгчмипеёдщвсзтжцыяъхаклуфй"),
                                                  list("чнпауэцкмейьгизборфлсжёювъхядщыт"),
                                                  list("чжъиздпюутьнхбрфкгцаломщяыеёвэсй"),
                                                  list("мюгыхнаутрифжъяёлоэчщьзйцвпкесдб")]]
rnd_ref = list('yruhqsldpxngokmiebfzcwvjat')
#rnd_ref_rus = list('рнъьпцяидмхтоэсщулйёбкюфачжезгыв')
reflectors = [list('yruhqsldpxngokmiebfzcwvjat'), list('дёряунчплегщьткимвфэбцхаюсыйоъжз')]
rnd_egn_rot_list = [Rotor(eng, i) for i in rnd_eng_list]
rot_key = ['1', '2', '3']
rotor1 = rnd_egn_rot_list[int(rot_key[0])]
rotor2 = rnd_egn_rot_list[int(rot_key[1])]
rotor3 = rnd_egn_rot_list[int(rot_key[2])]
reflector = Rotor(eng, rnd_ref)


# key = ('r', 'v', 'c')

def set_rotor(rot_key: List):
    '''Выбираются испульзуемые роторы из массива роторов, исходя из значений rot_key'''
    if len(rot_key) != 0:
        global rotor1
        global rotor2
        global rotor3
        rotor1 = rnd_egn_rot_list[int(rot_key[0])]
        rotor2 = rnd_egn_rot_list[int(rot_key[1])]
        rotor3 = rnd_egn_rot_list[int(rot_key[2])]


def crypt(ch: str, key: List):
    '''Шифрует символ, согласно алгоритму энигмы(в процессе доработки). key = ('a','b','c') - кортеж, содержащий три латинские буквы,
    соответсвующие смещению роторов, ch - шифруемый символ. Семещине соответсвует разности установленных смещений пердыдущего и используемого роторов.
    При обратном ходе алгоритм аналогичен, но меняестя знак смещения'''
    rot1_sh = eng.index(key[0])
    rot2_sh = eng.index(key[1])
    rot3_sh = eng.index(key[2])
    ch_1 = rotor1.ch_crpt(ch, rot1_sh)
    ch_2 = rotor2.ch_crpt(ch_1, rot2_sh - rot1_sh)
    ch_3 = rotor3.ch_crpt(ch_2, rot3_sh - rot2_sh)
    ch_ref = reflector.ch_crpt(ch_3, -rot3_sh)
    # print(ch_ref)
    ch_3r = rotor3.ch_crpt_rev(ch_ref, rot3_sh)
    # print(ch_3r)
    ch_2r = rotor2.ch_crpt_rev(ch_3r, -(rot3_sh - rot2_sh))
    # print(ch_2r)
    ch_1r = rotor1.ch_crpt_rev(ch_2r, -(rot2_sh - rot1_sh))
    # print(ch_1r)
    return eng[eng.index(ch_1r) - rot1_sh]


def text_crypt(text: str, key: Union[Tuple, List], com_key: dict = {}, transcript: bool = False):
    '''Шифрование текста. В этой версии неопознанные символы игнорируются'''
    if com_key == False:
        transcript = False
    text = text.lower()
    if transcript:
        text = flip(text, com_key)
    key = list(key)
    text = list(text)
    cr_text = ''
    n = 0
    m = 0
    k = 0
    for i in text:
        if i in eng:
            cr_text += crypt(i, key)
        else:
            cr_text += i
        n += 1
        if n > len(eng):
            n = 0
        key[0] = rotor1.Schr(key[0], 1, eng)

        if n % 2 == 0:
            m += 1
            if m > len(eng):
                m = 0
            key[1] = rotor1.Schr(key[1], 1, eng)

        if n % 3 == 0:
            k += 1
            if k > len(eng):
                k = 0
            key[2] = rotor1.Schr(key[2], 1, eng)
        # print(key, n,m,k)
    if transcript:
        return cr_text

    if com_key:
        return flip(cr_text, com_key)
    return cr_text


# com_key = {'a':'f','h':'d','l':'c'}

def flip(in_text: str, com_key: dict) -> str:
    in_text = list(in_text)
    new_str = ''

    def ch_fl(ch, com_key: dict):
        if ch in com_key.keys():
            return com_key[ch]
        if ch in com_key.values():
            return list(com_key.keys())[list(com_key.values()).index(ch)]
        else:
            return ch

    for i in in_text:
        new_str += ch_fl(i, com_key)
    return new_str


# ----------------------------------------Взаимодействие с пользователем------------------------------------------------
usr = 'Ввод --->'
usr_crpt: bool
usr_txt: str
usr_key: str = ''
usr_com_key = ''
rot_key = ['1', '2', '3']


def com_k(in_key: str) -> Union[dict, None]:
    in_key = in_key.replace(' ', '')
    com_key = {}
    for i in range(len(in_key)):
        if in_key[i] == '(':
            com_key[in_key[i + 1]] = in_key[i + 2]
            # print(in_key[i])
    for i, j in com_key.items():
        if i not in eng or j not in eng:
            return None
        else:
            return com_key


def show_st(a: Union[dict, List[Union[str]]]) -> str:
    st = ''
    if type(a) == list:
        for i in a:
            st += i
        return st
    if type(a) == dict:
        for i, j in a.items():
            st += '(' + i + j
        return st


if os.path.exists('enigma_data.pickle'):
    with open('enigma_data.pickle', 'rb') as f:
        save = pickle.load(f)
    rot_key = save[0]
    key = save[1]
    com_key = save[2]

set_rotor(rot_key)
save: list


class Switch():

    @staticmethod
    def set_mode():
        global save
        global rot_key
        global key
        global com_key
        global reflector
        global rnd_egn_rot_list

        reflector = Rotor(eng, rnd_ref)
        rot_key = input('роторы--->')
        rot_key = list(rot_key)
        set_rotor(rot_key)
        usr_key = input('ключ--->')
        key = list(usr_key.replace(' ', ''))
        usr_com_key = input('Замены букв--->')
        if len(usr_com_key) != 0:
            com_key = com_k(usr_com_key)
        else:
            com_key = False
        print(com_key)
        save = [rot_key, usr_key, com_key]

    @staticmethod
    def crypt():
        usr_txt = input('текст--->')
        cr_txt = text_crypt(usr_txt, key, com_key)
        print('\n', cr_txt)

    @staticmethod
    def transcr():
        usr_txt = input('текст--->')
        cr_txt = text_crypt(usr_txt, key, com_key, transcript=True)
        print('\n', cr_txt)

    @staticmethod
    def save_data():
        with open('enigma_data.pickle', 'wb') as f:
            pickle.dump(save, f)
        print('data_saved')

    @staticmethod
    def show_data():
        print('\nРоторы: {0}\n Ключ: {1}\nЗамены: {2}'.format(show_st(rot_key), key, show_st(com_key)))

    @classmethod
    def dispatch(cls, value):
        try:
            return getattr(cls, value)()
        except AttributeError:
            print('unknown command')


switch = Switch()

# -----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    print('''------------------------------------------------------------------------------------------------------------------------
    -----------------------------------------------------ЭНИГМА-------------------------------------------------------------
    ------------------------------------------------------------------------------------------------------------------------''')
    print(
        '\nПрограмма производит шифровку\расшифровку текста по алгоритму энигмы. \n Сначала необходимо установить параметры работы, для этого введите set_mode\n'
        ' Необходимо ввести ключ, номера роторов и параметры замены букв. Формат ввода: \n Ключ: "abc" - три строчные буквы без пробелов;'
        '\n Ротор:  "342" - три цифры, без пробелов (от 0 до 6)'
        '\nЗамента: (av(gb(hn(fg - пары строчных букв, разделяются правой скобкой, строка начинается с правой скобки'
        '\n Чтобы сохранить параметры работы введите: "save_data"\n Чтобы показать параметры: "show_data"\n "close" - Чтобы завершить работу программы\n\n'
        'Введите "crypt" - чтобы зашифровать текст; "transcr" - чтобы расшифровать')
    # -----------------------------------------------------------------------------------------------------------------------

    while True:

        key_word = input('input--->')

        if key_word.replace(' ', '') == 'close':
            break

        switch.dispatch(key_word.replace(' ', ''))
