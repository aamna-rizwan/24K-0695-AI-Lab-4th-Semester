#task2
import pandas as pd

data = {
    'email_text': [
        'Win money now click here',
        'Meeting at 5 pm please attend',
        'Congratulations you won a lottery',
        'Project deadline tomorrow',
        'Free gift card available now',
        'Let us schedule a call',
        'Earn dollars fast online',
        'Lunch tomorrow?',
        'Cheap loans available apply now',
        'Important update regarding your account'
    ],
    'label': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)
df.to_csv("emails.csv", index=False)

print("emails.csv created")

#task2
import pandas as pd

data = {
    'email_text': [
        'Win money now click here',
        'Meeting at 5 pm please attend',
        'Congratulations you won a lottery',
        'Project deadline tomorrow',
        'Free gift card available now',
        'Let us schedule a call',
        'Earn dollars fast online',
        'Lunch tomorrow?',
        'Cheap loans available apply now',
        'Important update regarding your account'
    ],
    'label': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)
df.to_csv("emails.csv", index=False)

print("emails.csv created")
