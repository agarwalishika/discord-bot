import discord
import os
import random
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!test'):
        await message.channel.send('what up party gurrrllll im up')

    if message.content.startswith('!commands'):
        await message.channel.send('!test, !hey do i got this?, !hey ca to in, !hey in to ca, !lets get?, !hey wyd, !hey spam, !hey send later')
    
    if message.content.startswith('!lets get?'):
        await message.channel.send('cRaCkaLAkIN hOmIE')

    if message.content.startswith('!hey spam'):
      command = message.content[10:].split(",")
      emoji = command[0]
      num = int(command[1])
      msg = ""
      for i in range(num):
        msg += emoji
      await message.channel.send(msg)

    if message.content.startswith('!hey wyd'):
        await message.channel.send('nothin\' much wyd?')
        msg = await client.wait_for('message')
        if "sad" in msg.content or "tired" in msg.content:
          await message.channel.send('oh noo, whats up?')
          await message.channel.send('can i help?')
          confirm = await client.wait_for('message')
          if "ye" in confirm.content:
            await message.channel.send('im listening')
            ans = await client.wait_for('message')
            responses = ['ok', 'ohhh', 'aww', 'oh no', 'ugh', 'sucks', 'mhmm']
            while "thanks" not in ans.content:
              await message.channel.send(random.choice(responses))
              ans = await client.wait_for('message')
            await message.channel.send('np bro hope you feel better <3')
          else:
            await message.channel.send('ok do me a favor - listen to music')
            await message.channel.send('hope you feel better soon <3')
        else:
          await message.channel.send('noice my dude')

    if message.content.startswith('!hey do i got this?'):
        await message.channel.send('You got this <3')
    
    if message.content.startswith('!hey ca to in?'):
      command = message.content[14:]
      currtime = command.split(":", 1)
      hour = int(currtime[0]) + 3
      if (hour > 12):
        hour = hour - 12
      val = "Time is {}:{}".format(hour, currtime[1])
      #val = "I got: {} and this is currtime: {}".format(command, currtime)
      await message.channel.send(val)

    if message.content.startswith('!hey in to ca?'):
      command = message.content[14:]
      currtime = command.split(":", 1)
      hour = int(currtime[0]) - 3
      if (hour < 0):
        hour = hour + 12
      val = "Time is {}:{}".format(hour, currtime[1])
      #val = "I got: {} and this is currtime: {}".format(command, currtime)
      await message.channel.send(val)

    if message.content.startswith('!hey send later'):
      command = message.content[15:].split(",")
      msg = command[0]
      numSeconds = int(command[1])

      import threading
      import asyncio
      class thread(threading.Thread):
        def __init__(self, msg, seconds, discord):
          threading.Thread.__init__(self)
          self.msg = msg
          self.seconds = seconds
          self.discord = discord
 
        # helper function to execute the threads
        async def run(self):
          import time
          time.sleep(self.seconds)
          await self.discord.channel.send(self.msg)
      
      thr = thread(msg, numSeconds, message)
      loop = asyncio.get_event_loop()
      loop.create_task(thr.run())
    
    if message.content.startswith('!hey define'):
      word = message.content[12:]
      from PyDictionary import PyDictionary
      dict = PyDictionary()
      await message.channel.send(dict.meaning(word))

    if message.content.startswith('!hey celebrate'):
      await message.channel.send('how much?')
      l = await client.wait_for('message')
      level = int(l.content)
      emojis = ['partying_face', 'star_struck', 'exploding_head', 'hugging', 'clap',
                'crown', 'star', 'star2', 'rainbow', 'medal', 'fireworks', 'sparkler', 'stars',
                'confetti_ball', 'tada', 'orange_heart', '100']
      
      import random
      times = random.randint(level,level*10)
      mess = ""
      for _ in range(times):
        em = random.randint(0, len(emojis)-1)
        mess = mess + ":" + emojis[em] + ": "
      
      await message.channel.send(mess)

keep_alive()
client.run(os.getenv('TOKEN'))