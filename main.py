import schedule
import time
import datetime
import argparse
from utils.reminders import check_for_new, send_high, send_urgent

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--authorization', type=str,
                        help='Linear API authorization key')
  parser.add_argument('--webhookurl', type=str, nargs="*",
                      help='Discord Webhook URL')
  parser.add_argument('--scanfreq', type=int, default=1,
                      help='How often minutes to scan for new issues')
  parser.add_argument('--urgentfreq', type=int, default=6,
                      help='How often (hours) to send reminders for urgent priority issues')
  parser.add_argument('--highfreq', type=int, default=15,
                      help='How often (hours) to send reminders for high priority issues')
  
  args = parser.parse_args()

  authorization = args.authorization
  webhookurl = args.webhookurl
  scanfreq = args.scanfreq
  urgentfreq = args.urgentfreq
  highfreq = args.highfreq

  assert scanfreq > 0, "Cannot scan every" + scanfreq + "seconds. Minimum scan frequency: every 1 minute."
  assert urgentfreq > 0, "Cannot send urgent priority alerts every" + urgentfreq + "hours. Minimum alert frequency: every 1 hour."
  assert urgentfreq > 0, "Cannot send high priority alerts every" + highfreq + "hours. Minimum alert frequency: every 1 hour."
  
  last_time = datetime.datetime.now()
  schedule.every(scanfreq).minutes.do(check_for_new, last_time, authorization, webhookurl)
  schedule.every(urgentfreq).hours.do(send_urgent, authorization, webhookurl)
  schedule.every(highfreq).hours.do(send_high, authorization, webhookurl)
  
  while True:
    schedule.run_pending()
    time.sleep(1) 
