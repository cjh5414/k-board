from .base import FunctionalTest


class ModifyPostTest(FunctionalTest):
    def test_modify_post(self):
        self.browser.get(self.live_server_url)
        self.move_to_default_board()

        # 지훈이는 'django' 대한 게시글을 작성한다.
        self.add_post('jango', 'Hello jango')

        # 게시글의 오타를 발견하고 수정하려고 한다.
        # 해당하는 게시글을 클릭하여 이동한 후 수정 버튼을 누른다.
        table = self.browser.find_element_by_id('id_post_list_table')
        rows = table.find_elements_by_css_selector('tbody > tr > td > a')
        rows[0].click()

        self.browser.find_element_by_id('id_modify_post_button').click()

        # 작성되어 있던 게시글이 보인다.
        titlebox = self.browser.find_element_by_id('id_new_post_title')
        self.assertEqual(titlebox.text, 'jango')

        contentbox = self.get_contentbox()
        self.assertEqual(contentbox.text, 'Hello jango')

        # 제목과 내용의 'jango' 오타를 올바르게 수정한다.
        titlebox.clear()
        titlebox.send_keys('django')

        contentbox.clear()
        contentbox.send_keys('Hello django')
        self.browser.switch_to.default_content()

        # 실수로 '취소' 버튼을 누른다.
        response = self.browser.find_element_by_id('id_cancel_button').click()

        # 제목과 내용이 변경되지 않고 그대로이다.
        table = self.browser.find_element_by_id('id_post_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertNotContains(self, response, 'django')

        # 다시 수정하고
        titlebox = self.browser.find_element_by_id('id_new_post_title')
        titlebox.clear()
        titlebox.send_keys('django')

        contentbox = self.get_contentbox()
        contentbox.clear()
        contentbox.send_keys('Hello django')
        self.browser.switch_to.default_content()

        # 이번에는 제대로 '확인' 버튼을 누른다.
        submit_button = self.browser.find_element_by_css_selector('button[type="submit"]')
        response = submit_button.click()

        # 제목과 내용이 변경된 것을 확인한다.
        table = self.browser.find_element_by_id('id_post_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertContains(self, response, 'django')
