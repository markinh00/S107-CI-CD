import unittest
import xmlrunner

from tests.test_teacher_schedule import TestTeacherSchedule1
from tests.test_teacher_schedule_api import TestTeacherSchedule2
from tests.test_teacher_schedule_building import TestTeacherScheduleBuilding, TestTeacherScheduleBuildingWrong


# Cria o TestSuite para rodar todos os testes juntos
def run_all_tests():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Adiciona as classes de teste
    suite.addTests(loader.loadTestsFromTestCase(TestTeacherSchedule1))
    suite.addTests(loader.loadTestsFromTestCase(TestTeacherSchedule2))
    suite.addTests(loader.loadTestsFromTestCase(TestTeacherScheduleBuilding))
    suite.addTests(loader.loadTestsFromTestCase(TestTeacherScheduleBuildingWrong))

    # Salva o resultado dos testes em arquivos XML
    with open('test_results.xml', 'wb') as output:
        xmlrunner.XMLTestRunner(output=output).run(suite)


if __name__ == '__main__':
    run_all_tests()
