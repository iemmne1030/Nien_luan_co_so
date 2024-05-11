import os.path
from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import json
from langdetect import detect




class action_name_month_year(Action):
    def name(self) -> Text:
        return "action_name_month_year"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        lt_month = int(tracker.get_slot("lt_month"))
        lt_year = int(tracker.get_slot("lt_year"))
        # lt_date = int(tracker.get_slot("lt_date"))

        print(lt_month)
        print(lt_year)

        # Lấy dữ liệu từ JSON hoặc nguồn dữ liệu khác
        file_path = os.path.join(os.path.dirname(__file__) , r"C:\Users\PC\PycharmProjects\chatbot_N\cttn.json")
        with open(file_path, "r", encoding="utf-8") as file:
            json_data = json.load(file)

        filtered_events = []
        for event_data in json_data:
            month = event_data["month"]
            year = event_data["year"]
            # date = event_data["date"]

            if month == lt_month and year == lt_year:
                filtered_events.append(event_data)

        # Tiếp tục xử lý với danh sách sự kiện đã lọc
        if filtered_events:
            event_names = [event_data["name"] for event_data in filtered_events]
            ans = ", ".join(event_names)
            answer = "Trong tháng " + str(lt_month) + " năm " + str(lt_year) + " có công trình: " + ans
        else:
            answer = "Không có sự kiện nào trong tháng và năm được yêu cầu."

        dispatcher.utter_message(text=answer)

        return [SlotSet("lt_month", lt_month), SlotSet("lt_year", lt_year)]

class action_member_name(Action):
    def name(self) -> Text:
        return "action_member_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        lt_name = tracker.get_slot("lt_name")

        print(lt_name)
        print(type(lt_name))

        #đọc dữ liệu
        file_path = os.path.join(os.path.dirname(__file__), r"C:\Users\PC\PycharmProjects\chatbot_N\cttn.json")
        with open(file_path, "r", encoding="utf-8") as file:
            json_data = json.load(file)

            members = None
            for event in json_data:
                if event["name"] == lt_name.capitalize():
                    members = event["member"]
                    break
            print(members)

        if members is not None:
            dispatcher.utter_message(f"Sự kiện {lt_name} có {members} thành viên")
        else:
            dispatcher.utter_message(f"Không tồn tại sự kiện hoặc không có thành viên.")

        return [SlotSet("lt_name", lt_name)]

class action_done_name(Action):
    def name(self) -> Text:
        return "action_done_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        lt_name = tracker.get_slot("lt_name")

        print(lt_name)
        print(type(lt_name))

        #đọc dữ liệu
        file_path = os.path.join(os.path.dirname(__file__), r"C:\Users\PC\PycharmProjects\chatbot_N\cttn.json")
        with open(file_path, "r", encoding="utf-8") as file:
            json_data = json.load(file)

            dones = None
            for event in json_data:
                if event["name"] == lt_name.capitalize():
                    dones = event["done"]
                    break
            print(dones)

        if dones is not None:
            dispatcher.utter_message(f"Sự kiện {lt_name} {dones}")
        else:
            dispatcher.utter_message(f"Không tồn tại sự kiện hoặc không có thành viên.")

        return [SlotSet("lt_name", lt_name)]

class action_place_name(Action):
    def name(self) -> Text:
        return "action_place_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        lt_name = tracker.get_slot("lt_name")

        print(lt_name)
        print(type(lt_name))

        # đọc dữ liệu
        file_path = os.path.join(os.path.dirname(__file__), r"C:\Users\PC\PycharmProjects\chatbot_N\cttn.json")
        with open(file_path, "r", encoding="utf-8") as file:
            json_data = json.load(file)

            places = None
            for event in json_data:
                if event["name"] == lt_name.capitalize():
                    places = event["place"]
                    break
            print(places)

        if places is not None:
            dispatcher.utter_message(f"Sự kiện {lt_name} có {places}")
        else:
            dispatcher.utter_message(f"Không tồn tại sự kiện hoặc không có thành viên.")

        return [SlotSet("lt_name", lt_name)]

class action_time_name(Action):
    def name(self) -> Text:
        return "action_time_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        lt_name = tracker.get_slot("lt_name")

        print(lt_name)
        print(type(lt_name))

        #đọc dữ liệu
        file_path = os.path.join(os.path.dirname(__file__), r"C:\Users\PC\PycharmProjects\chatbot_N\cttn.json")
        with open(file_path, "r", encoding="utf-8") as file:
            json_data = json.load(file)

            time_tg = None
            for event in json_data:
                if event["name"] == lt_name.capitalize():
                    time_tg = event["time"]
                    break
            print(time_tg)

        if time_tg is not None:
            dispatcher.utter_message(f"Sự kiện {lt_name} bắt đầu lúc {time_tg} ")
        else:
            dispatcher.utter_message(f"Không tồn tại sự kiện hoặc không có thành viên.")

        return [SlotSet("lt_name", lt_name)]

class action_name_inf(Action):
    def name(self) -> Text:
        return "action_name_inf"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        lt_name = tracker.get_slot("lt_name")

        print(lt_name)
        print(type(lt_name))

        # Lấy dữ liệu từ JSON hoặc nguồn dữ liệu khác
        file_path = os.path.join(os.path.dirname(__file__) , r"C:\Users\PC\PycharmProjects\chatbot_N\cttn.json")
        with open(file_path, "r", encoding="utf-8") as file:
            json_data = json.load(file)

        # filtered_events = []
        for event_data in json_data:
            if event_data["name"] == lt_name.capitalize():
                # name = event_data["name"]
                month = event_data["month"]
                year = event_data["year"]
                date = event_data["date"]
                time = event_data["time"]
                place = event_data["place"]
                member = event_data["member"]
                done = event_data["done"]
                dispatcher.utter_message(f"Sự kiện {lt_name} được tổ chức vào ngày {date} tháng {month} năm {year} ở {place} bắt đầu lúc {time} với {member} thành viên")
            else:
                dispatcher.utter_message(f"Không tồn tại sự kiện hoặc không có thành viên.")

            return [SlotSet("lt_name", lt_name)]


class action_fall_message(Action):
    def name(self) -> Text:
        return "action_fall_message"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Xử lý logic hoặc gửi tin nhắn thông báo khi không thể xác định intent
        response = "Xin lỗi, tôi không hiểu câu hỏi của bạn."

        dispatcher.utter_message(text=response)
        return []