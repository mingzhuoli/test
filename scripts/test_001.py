import allure, pytest

class Test_abc:
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="我是测试001")
    def test_001(self):
        allure.attach("描述", "我在测试001里面")
        assert 1
    @pytest.mark.skip(2>1, "测试")
    def test_002(self):
        assert 0