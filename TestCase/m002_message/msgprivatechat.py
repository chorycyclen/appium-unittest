import random
import time
from library.core.TestCase import TestCase
from library.core.utils.applicationcache import current_mobile
from preconditions.BasePreconditions import LoginPreconditions
from library.core.utils.testcasefilter import tags
from pages import *


class Preconditions(LoginPreconditions):
    """前置条件"""

    @staticmethod
    def enter_message_page(reset=False):
        """进入消息页面"""
        # 登录进入消息页面
        Preconditions.make_already_in_message_page(reset)


class MsgPrivateChatMsgList(TestCase):
    """
    模块：单聊->消息列表
    文件位置：全量/10.整理全量测试用例---黄彩最.xlsx
    表格：单聊
    """

    @classmethod
    def setUpClass(cls):
        pass

    def default_setUp(self):
        """确保每个用例运行前在消息页面"""
        Preconditions.select_mobile('Android-移动')
        mess = MessagePage()
        if mess.is_on_this_page():
            return
        else:
            current_mobile().reset_app()
            Preconditions.enter_message_page()

    @tags('ALL', 'SMOKE', 'CMCC')
    def test_Msg_PrivateChat_MsgList_0001(self):
        """消息-消息列表进入"""
        # 1、点击消息
        mess = MessagePage()
        mess.open_message_page()
        if not mess.is_on_this_page():
            raise AssertionError("未成功进入消息列表页面")

    @tags('ALL', 'SMOKE', 'CMCC')
    def test_Msg_PrivateChat_MsgList_0002(self):
        """消息-消息列表界面+功能页面元素检查"""
        # 1、点击消息
        mess = MessagePage()
        mess.open_message_page()
        # 2、点击右上角的+号按钮
        mess.click_add_icon()
        time.sleep(1)
        # 下拉出“新建消息”、“免费短信”、“发起群聊”、分组群发、“扫一扫”，入口
        mess.page_should_contain_text("新建消息")
        mess.page_should_contain_text("免费短信")
        mess.page_should_contain_text("发起群聊")
        mess.page_should_contain_text("扫一扫")
        mess.driver.back()
        mess.wait_for_page_load()

    @tags('ALL', 'SMOKE', 'CMCC')
    def test_Msg_PrivateChat_MsgList_0004(self):
        """消息-消息列表界面新建消息页面元素检查"""
        # 1、点击消息右上角+按钮
        mess = MessagePage()
        mess.open_message_page()
        mess.click_add_icon()
        # 2、查看新建消息页面元素
        # 左上角有返回按钮，左上角显示新建消息标题，下方有搜索输入框，
        # 和通讯录入口，全量联系人列表，左侧显示姓名首字母排序、右侧显示索引字母排序。
        mess.click_new_message()
        scp = SelectContactsPage()
        scp.wait_for_create_msg_page_load()
        scp.page_contain_element('返回')
        scp.page_contain_element('选择联系人')
        scp.page_contain_element('搜索或输入手机号')
        scp.page_contain_element('右侧字母索引')
        if not scp.is_right_letters_sorted():
            raise AssertionError("右侧字母索引未排序")
        scp.page_contain_element('左侧字母索引')
        if not scp.is_left_letters_sorted():
            raise AssertionError("左侧字母索引未排序")
        # 3、滑动屏幕, 搜索栏常驻顶端
        scp.page_up()
        scp.page_up()
        scp.page_contain_element('搜索或输入手机号')
        scp.click_back()
        mess.wait_for_page_load()

    @tags('ALL', 'SMOKE', 'CMCC')
    def test_Msg_PrivateChat_MsgList_0005(self):
        """消息-消息列表界面新建消息页面返回操作"""
        # 1、点击右上角的+号按钮，成功进入新建消息界面
        mess = MessagePage()
        mess.click_add_icon()
        mess.click_new_message()
        # 2、点击左上角返回按钮，退出新建消息，返回消息列表
        scp = SelectContactsPage()
        scp.wait_for_create_msg_page_load()
        scp.click_back()
        mess.wait_for_page_load()

    @tags('ALL', 'SMOKE', 'CMCC')
    def test_Msg_PrivateChat_MsgList_0006(self):
        """消息-消息列表界面新建消息页面返回操作"""
        # 1、点击右上角的+号按钮
        mess = MessagePage()
        mess.click_add_icon()
        mess.click_new_message()
        # 2、点击手机系统内置返回返回按钮
        scp = SelectContactsPage()
        scp.wait_for_create_msg_page_load()
        scp.driver.back()
        mess.wait_for_page_load()

    @tags('ALL', 'SMOKE', 'CMCC')
    def test_Msg_PrivateChat_MsgList_0007(self):
        """资料页发起聊天"""
        # 1、在“联系人资料”页 点击【消息】,进入“个人会话”窗口
        Preconditions.enter_private_chat_page()
        # 返回消息列表页面
        chat = SingleChatPage()
        mess = MessagePage()
        chat.click_back()
        ContactDetailsPage().click_back()
        mess.open_message_page()
        mess.wait_for_page_load()

    @staticmethod
    def setUp_test_Msg_PrivateChat_MsgList_0008():
        """消息列表点击消息记录前，先发送一条消息"""
        Preconditions.enter_private_chat_page()
        chat = SingleChatPage()
        chat.input_message("hello")
        chat.send_message()
        chat.click_back()
        ContactDetailsPage().click_back()
        mess = MessagePage()
        mess.open_message_page()
        mess.wait_for_page_load()

    @tags('ALL', 'SMOKE', 'CMCC')
    def test_Msg_PrivateChat_MsgList_0008(self):
        """消息-消息列表进入到会话页面"""
        # 1、在消息列表点击消息记录，进入到会话页面
        mess = MessagePage()
        mess.click_msg_by_content("hello")
        chat = SingleChatPage()
        chat.wait_for_page_load()
        chat.click_back()
        mess.wait_for_page_load()

    @staticmethod
    def setUp_test_Msg_PrivateChat_MsgList_0010():
        """消息列表点击消息记录前，先发送一条消息"""
        Preconditions.enter_private_chat_page()
        chat = SingleChatPage()
        chat.input_message("hello")
        chat.send_message()
        chat.click_back()
        ContactDetailsPage().click_back()
        mess = MessagePage()
        mess.open_message_page()
        mess.wait_for_page_load()

    @tags('ALL', 'SMOKE', 'CMCC')
    def test_Msg_PrivateChat_MsgList_0010(self):
        """消息-消息列表-消息列表显示未发送成功"""
        # 1、 在会话页面输入文本消息
        mess = MessagePage()
        mess.click_msg_by_content("hello")
        chat = SingleChatPage()
        chat.wait_for_page_load()
        # 断网
        current_mobile().set_network_status(0)
        chat.input_message("MsgList_0010")
        # 2、点击发送
        chat.send_message()
        if not chat.is_msg_send_fail():
            raise AssertionError("断网发送消息，在聊天会话窗无发送失败标志")
        # 3、点击返回消息列表
        chat.click_back()
        mess.wait_for_page_load()
        if not mess.is_iv_fail_status_present():
            raise AssertionError("断网发送消息，在消息列表无发送失败标志")

    @staticmethod
    def tearDown_test_Msg_PrivateChat_MsgList_0010():
        """恢复网络连接"""
        current_mobile().set_network_status(6)