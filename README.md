# Enigma-crypter
An application that performs encryption and decryption using the enigma algorithm

Run __main__ to use GUI. Run enigma_console for console version. 
Before encrypt /decrypt text you should enter some key in the right text fileds or generate it.
Program uses key from text fields or last saved key if text fields are empty. 

key structure:
  rotors: three digits from one to six
  key: three english letters
  letter replacements: pairs of letters or symbols separated by space
 
buttons:
  show: shows last saved key in the text fields
  generate: generates random key and shows it
  save: saves key in from the text fields
  
  Encrypt:
  encrypts text using current key. If "Read from file" box is checked text will be read from 
  file the path to which is specified in the upper text field. If "Save into file" box is checked 
  text will be written to file the path to which is specified in the lower text field. If no boxes checked
  text reads and outputs directly from text fields.
  
  Transcrypt: same functionality as Encrypt but performs decryption using currnet key.
