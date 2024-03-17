import aiohttp
import asyncio

async def get_ip_address_from_discord_id(discord_id: str) -> str:
    """
    Function to retrieve the IP address associated with a Discord user ID.

    Parameters:
    - discord_id: str
        The Discord user ID for which the IP address is to be fetched.

    Returns:
    - str
        The IP address associated with the provided Discord user ID.

    Raises:
    - ValueError:
        If the Discord ID is invalid or not found, an error is raised.
    """

    # Discord API endpoint to fetch user data
    url = f"https://discord.com/api/v9/users/{discord_id}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                user_data = await response.json()
                ip_address = user_data.get('ip', 'IP Address not found')
                return ip_address
            else:
                raise ValueError(f"Failed to retrieve IP address. Status code: {response.status}")

async def main():
    discord_id = input("Enter Discord user ID: ")
    try:
        ip_address = await get_ip_address_from_discord_id(discord_id)
        print(f"The IP address associated with Discord ID {discord_id} is: {ip_address}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
