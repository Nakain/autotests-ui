import pytest
import random


# Перезапуск тестов. Перезапускаем только нестабильные тесты
@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_reruns():
    assert random.choice([True, False])


PLATFORM = 'Windows'


@pytest.mark.flaky(reruns=3, reruns_delay=2)
class TestReruns:
    def test_reruns_1(self):
        assert random.choice([True, False])

    def test_reruns_2(self):
        assert random.choice([True, False])

#Перезапуск автотеста с условием
@pytest.mark.flaky(reruns=3, reruns_delay=2, condition=PLATFORM == 'Windows')
def test_rerun_with_conditions():
    assert random.choice([True, False])
