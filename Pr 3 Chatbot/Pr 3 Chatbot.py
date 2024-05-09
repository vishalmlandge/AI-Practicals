from datetime import datetime
import random

track_order_data = {
    "vishal@mail.com": "on the way",
    "rahul@mail.com": "delivered",
    "abcd@mail.com": "preparing",
}

today_recommendation = [
    {
        "name": "Pizza",
        "price": 299
    },
    {
        "name": "Garlic Bread",
        "price": 159
    },
    {
        "name": "Chicken Wings",
        "price": 159
    },
    {
        "name": "Pasta",
        "price": 180
    },
    {
        "name": "Salad",
        "price": 120
    },
    {
        "name": "Ice Cream",
        "price": 80
    },
    {
        "name": "Cold Coffee",
        "price": 80
    },
]

restaurant_data = {
    "users": [
        {
            "uid": "1234567890",
            "name": "vishal",
            "email": "vishal@mail.com",
            "city": "NY",
            "recent_orders": [
                {
                    "oid": "123",
                    "order_item_name": "Salad",
                    "price": 120
                },
                {
                    "oid": "456",
                    "order_item_name": "Cold Coffee",
                    "price": 80
                },
                {
                    "oid": "789",
                    "order_item_name": "Chicken Wings",
                    "price": 159
                }
            ],
            "favorites": [
                {
                    "oid": "123",
                    "order_item_name": "Salad",
                    "price": 120
                },
            ]
        },
        {
            "uid": "0987654321",
            "name": "rahul",
            "email": "rahul@mail.com",
            "city": "LA",
            "recent_orders": [
                {
                    "oid": "789",
                    "order_item_name": "Chicken Wings",
                    "price": 159
                }
            ],
            "favorites": [
                {
                    "order_item_name": "Pizza",
                    "price": 299
                },
            ]
        },
        {
            "uid": "0987654321",
            "name": "ABCD",
            "email": "abcd@mail.com",
            "city": "NY",
            "recent_orders": [
                {
                    "oid": "789",
                    "order_item_name": "Chicken Wings",
                    "price": 159
                }
            ],
            "favorites": [
                {
                    "order_item_name": "Garlic Bread",
                    "price": 159
                }
            ]
        }
    ],
    "menu items": [
        {
            "name": "Pizza",
            "price": 299
        },
        {
            "name": "Garlic Bread",
            "price": 159
        },
        {
            "name": "Chicken Wings",
            "price": 159
        },
        {
            "name": "Pasta",
            "price": 180
        },
        {
            "name": "Salad",
            "price": 120
        },
        {
            "name": "Ice Cream",
            "price": 80
        },
        {
            "name": "Cold Coffee",
            "price": 80
        },
    ],
    "restaurants": [
        {
            "id": 0,
            "branch_name": "ApnaDhaba Downtown",
            "contact_no": "+1 (555) 123-4567",
            "email": "downtown@ApnaDhaba.com",
            "address": "123 Main Street, Downtown, City, State, ZIP"
        },
        {"id": 1,
         "branch_name": "ApnaDhaba Heights",
         "contact_no": "+1 (555) 987-6543",
         "email": "heights@ApnaDhaba.com",
         "address": "456 Hill Avenue, Heights, City, State, ZIP"
         },
        {
            "id": 2,
            "branch_name": "ApnaDhaba Lakeside",
            "contact_no": "+1 (555) 789-0123",
            "email": "lakeside@ApnaDhaba.com",
            "address": "789 Lakeview Drive, Lakeside, City, State, ZIP"
        }
    ]
}

time_now = datetime.now()
current_hour = time_now.hour

print("\n****** Welcome to ApnaDhaba ******")
name = input("\nEnter your Name :")

if (current_hour < 12):
    print("\nGood Morning, ", name)
elif (current_hour >= 12 & current_hour < 16):
    print("\nGood Afternoon, ", name)
elif (current_hour >= 16 & current_hour < 19):
    print("\nGood Evening, ", name)
else:
    print("\nHello, ", name)


def show_stores():
    for restaurant in restaurant_data['restaurants']:
        print("  Name : ", restaurant['branch_name'])
        print("  ID : ", restaurant['id'])
    print("")


def show_menu():
    for menu_item in restaurant_data['menu items']:
        print("  Name :", menu_item['name'])
        print("  Price :", menu_item['price'])


def get_contact_info(res_id):
    restaurant = restaurant_data['restaurants'][res_id]
    print("  Name : ", restaurant['branch_name'])
    print("  Contact No : ", restaurant['contact_no'])
    print("  Email : ", restaurant['email'])
    print("  Address : ", restaurant['address'])


def get_recent_orders():
    email = input("Enter your Email : ")
    for user in restaurant_data["users"]:
        if user["email"] == email:
            for item in user["recent_orders"]:
                print("Order Item Name : ", item["order_item_name"])
                print("Price : ", item["price"])
        else:
            return None


def get_favorites():
    email = input("Enter your Email : ")
    for user in restaurant_data["users"]:
        if user["email"] == email:
            for item in user["favorites"]:
                print("Favorite Item Name : ", item["order_item_name"])
                print("Favorite Item Price : ", item["price"])
        else:
            return None


def todays_special():
    tds = random.randint(0, 5)
    print("Today's Recommendation")
    print("  Name : ", today_recommendation[tds]["name"])
    print("  Price : ", today_recommendation[tds]["price"])



def feedback():
    print("\n-----------------Your Feedback is the Key to Development for us !!------------------------\n")
    like = input("Q1. Did you like our service ?? (yes / no) : ")
    if (like == "yes"):
        print("We are greatful to provide you your meal")
    elif (like == "no"):
        print("Ohh !! , Thank you for such a honest answer, we will try to improve ourself")
    else:
        print("Please give answer in yes or no")

    meal = input("Q2. How Was Your Meal ?? (great/good/bad/average/not so good/worst)")
    if (meal == "great"):
        print("hey !!, i like that too, same pinch dude !!")
    elif (meal == "good"):
        print("i'm Happy to hear that from you. ")
    elif (meal == "bad"):
        print("Ohh !, i'm sorry for suggesting that to you")
    elif (meal == "average"):
        print("i Hope you will definitely like that next time")
    elif (meal == "not so good"):
        print("I Apologies for your Inconvenience😣, We will try to suggest uhh some amazing food, I promise")
    else:
        print("Please enter input from given options")

    rate = int(input("Q3. How you rate our service from 1 to 5 : "))
    if (rate == 1):
        print("😑")
    elif (rate == 2):
        print("🙂")
    elif (rate == 3):
        print("😊")
    elif (rate == 4):
        print("😄")
    elif (rate == 5):
        print("😁")
    else:
        print("Please Enter Digit from 1 to 5 ")

    print("Thank You for your answer 🙏")

    sugg = input("Q4. Any suggestion for us ?? : ")
    print("Thank You for your feedback 👍")


def get_offers():
    print("\n----------------------Offers That you Might be Like 💥-----------------------")
    print("1. Refer to your friend and get 200 in your ApnaDhaba Wallet ")
    print("2. 50% Discount on your First Meal ")
    print("3. 20% off on order of Rs.500+ ")
    print("4. Use Code PIYUSH for 30% Discount ")



def track_order():
    email = input("Enter your email : ")
    try:
        print(track_order_data[email])
    except:
        print("Please enter correct UID")



for x in range(0, 10):
    ch = input(
        "\nWhat should I help you with \n 1.Show Menu\n 2.Stores Near Me\n 3.Contact Store\n 4.Queries and Feedback\n 5.View my recent orders (LOG IN)\n 6.View my favorites (LOG IN)\n 7.Track My Order\n 8.Today's Recommendation\n 9.Offers \nEnter your Choice: ")
    if (ch == "1"):
        show_menu()
    elif (ch == "2"):
        show_stores()
    elif (ch == "3"):
        try:
            res_ch = int(input("Enter the restaurant id : "))
            get_contact_info(res_ch)
        except:
            print("Enter a valid restaurant ID")
    elif (ch == "4"):
        feedback()
    elif (ch == "5"):
        get_recent_orders()
    elif (ch == "6"):
        get_favorites()
    elif (ch == "7"):
        track_order()
    elif (ch == "8"):
        todays_special()
    elif (ch == "9"):
        get_offers()
    else:
        print("Enter a valid option")