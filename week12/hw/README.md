# Reminder Program

## About
This is a small reminder program. You can make simple, meeting, or daily reminders.  
The program saves all reminders in a JSON file.

## Features
- Simple reminder  
- Meeting reminder with participants  
- Daily reminder (repeat)  
- Show all reminders  
- Find reminder by ID  
- Run all reminders  
- Group reminders by type  

## How to Use
Run the program:

```
python main.py
```

Menu options:

1. Make new reminder  
2. Remove reminder  
3. Show all reminders  
4. Find reminder by ID  
5. Run all reminders  
6. Group by type  
7. Exit  

## Files
- main.py  
- reminder_model.py  
- logger.py  
- utils.py  
- id_generator.py  
- config.py  
- activity.log  

## Example

### Creating a Meeting Reminder

```
Choose: 1          # Create new reminder
Type: 2            # Meeting reminder
Reminder: Team meeting
Participants: Ali-Sara
Timer: 15:30
```

**Result:**
```
Created a 'meeting' reminder:
- Reminder: Team meeting
- Time: 15:30
- Participants: Ali, Sara
```

## Version
v2.0.0
