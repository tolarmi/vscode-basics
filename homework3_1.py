from datetime import datetime

def get_days_from_today(date):
    try:
        
        input_date = datetime.strptime(date, '%Y-%m-%d')
      
        current_date = datetime.today()
        
        difference = input_date - current_date
        
        return difference.days
    
    except ValueError:
        print("Неправильний формат вхідних даних. Потрібно використовувати формат 'РРРР-ММ-ДД'.")
        return None