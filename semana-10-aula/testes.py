import unittest
import numeroromano as nr

class NumeroRomanoTest(unittest.TestCase):

  def setUp(self):
    print('Teste', self._testMethodName, 'sendo executado...')

  def tearDown(self):
    print('Teste', self._testMethodName, 'finalizado.')

  def testI(self):
    self.assertEqual(1, nr.converte('I'), 'Erro ao converter I')

  def testV(self):
    self.assertEqual(5, nr.converte('V'), 'Erro ao converter V')

  def testII(self):
    self.assertEqual(2, nr.converte('II'), 'Erro ao converter II')

  def testXXII(self):
    self.assertEqual(22, nr.converte('XXII'), 'Erro ao converter XXII')

  def testIX(self):
    print('Esse teste apontava um erro, agora corrigido')
    self.assertEqual(9, nr.converte('IX'), 'Erro ao converter IX')

  def testXXIV(self):
    print('Esse teste apontava um erro, agora corrigido')
    self.assertEqual(24, nr.converte('XXIV'), 'Erro ao converter XXIV')

if __name__ == "__main__":
  unittest.main()
