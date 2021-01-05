import discord

guild_id = 
color_anchor = 
category_anchor = 
class_anchor = 
everyone_id =
bot_token = 
command_channel_id = 
command_channel_name =


class MyClient(discord.Client):
    async def on_ready(self):
        print("Tiny Ygg is alive!\nPlease reach out to Myon#5180 if you need any assistance.")
    async def on_message(self, message):
        #Ensures the bot does not respond to itself
        if message.author.id == self.user.id:
            return
        else:
            #Segregates the channel functions, deep_city is used exclusively for role management
            if (str(message.channel) == command_channel_name) or (str(message.channel.id) == command_channel_id):

                #Tries to split the command, if it unable to, or if any variables in acceptable_commands are 
                #absent within the first part chain terminates and user is told to rewrite request
                try:
                    acceptable_commands = ["set", "rem", "lis"]
                    split_message = str(message.content).lower().split(" ", 1)
                    if not any(x in split_message[0] for x in acceptable_commands):
                        print("exception raised")
                        raise Exception
                except:
                    print("Not given usable command")
                    await message.channel.send('Please make sure your message is in the format \"[action(set/remove)] [role name]\"'.format(message))
                    return

                guild = client.get_guild(guild_id)
                color_anchor = guild.get_role(color_anchor)
                category_anchor = guild.get_role(category_anchor)
                class_anchor = guild.get_role(class_anchor)
                everyone_id = guild.get_role(everyone_id)
                color_roles = [r for r in guild.roles if color_anchor > r > category_anchor]
                category_roles = [r for r in guild.roles if category_anchor > r > class_anchor]
                class_roles = [r for r in guild.roles if class_anchor > r > everyone_id]

                if 'set' in split_message[0]:
                    selected_role = list(filter(lambda role: role.name.casefold() == split_message[1], message.guild.roles))[0]
                    if selected_role in color_roles:
                        roleType = "color "
                    elif selected_role in category_roles:
                        roleType = "utility "
                    elif selected_role in class_roles:
                        roleType = "class "
                    else:
                        await message.channel.send('Hi ' + str(message.author.name) + '! The role **' + str(selected_role) + '** does not seem to be an available role.'.format(   message))
                        return
                    holder = 0
                    for role in message.author.roles:
                        if role in color_roles and selected_role in color_roles:
                            await message.author.remove_roles(role)
                            await message.author.add_roles(selected_role)
                            await message.channel.send('Hi ' + str(message.author.name) + '! I have removed the color **' + str(role) + '** and added the ' + roleType + "**" + str(selected_role) + '** for you.'.format(   message))
                            holder = 1
                            break
                        elif role in class_roles and selected_role in class_roles:
                            await message.author.remove_roles(role)
                            await message.author.add_roles(selected_role)
                            await message.channel.send('Hi ' + str(message.author.name) + '! I have removed the class **' + str(role) + '** and added the ' + roleType + "**" + str(selected_role) + '** for you.'.format(   message))
                            holder = 1
                            break
                    if not holder == 1:
                        await message.author.add_roles(selected_role)
                        await message.channel.send('Hi ' + str(message.author.name) + '! I have added the ' + roleType + "**" + str(selected_role) + '** for you.'.format(   message))                    #def check(reaction, user):
                elif 'rem' in split_message[0]:
                    selected_role = list(filter(lambda role: role.name.casefold() == split_message[1], message.guild.roles))[0]
                    try:
                        await message.author.remove_roles(selected_role)
                        await message.channel.send('Hi ' + str(message.author.name) + '! I have removed the role **' + str(selected_role) + '** for you. '.format(message))
                    except:
                        await message.channel.send('Sorry ' + str(message.author.name) + '! I wasn\'t able to remove your role. Please reach out to the mod team so they can fix this.'.format(message))
                elif 'lis' in split_message[0]:
                    curRoles = []
                    msg = "```Colors (1 max)\n---------------------\n"
                    for role in color_roles:
                        curRoles.append(str(role)+", ")
                    curRoles.sort()
                    curRoles[-1] = str(curRoles[-1])[:-2]
                    for item in curRoles:
                        msg += str(item)
                    msg += "\n\n"
                    curRoles = []
                    msg += "Classes (1 max)\n---------------------\n"
                    for role in class_roles:
                        curRoles.append(str(role)+", ")
                    curRoles.sort()
                    curRoles[-1] = str(curRoles[-1])[:-2]
                    for item in curRoles:
                        msg += str(item)
                    msg += "\n\n"
                    curRoles = []
                    msg += "Categories\n---------------------\n"
                    for role in category_roles:
                        curRoles.append(str(role)+", ")
                    curRoles.sort()
                    curRoles[-1] = str(curRoles[-1])[:-2]
                    for item in curRoles:
                        msg += str(item)
                    msg += "```"
                    await message.channel.send(msg.format(message))
                else:
                    return
            if str(message.channel.id) == command_channel:
                guild = client.get_guild(guild_id)
                new_member = discord.utils.get(guild.roles, name="new adventurer")
                acceptable_commands = "accept"
                if "accept" in str(message.content).strip().lower():
                    await message.author.remove_roles(new_member)
                    acceptLog(message)

intents = discord.Intents.default()
intents.members = True
client = MyClient(intents=intents)
client.run(bot_token)
