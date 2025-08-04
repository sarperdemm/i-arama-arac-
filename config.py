import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# Redmine Configuration
REDMINE_API_KEY = os.getenv('REDMINE_API_KEY', '269f774a9558855be059264153f94bd5293bc694')
REDMINE_API_URL = os.getenv('REDMINE_API_URL', 'https://r.ebalina.com')

# Mattermost Configuration
MATTERMOST_TOKEN = os.getenv('MATTERMOST_TOKEN', 'k9huwxdwk78xxybd94da6s838h')
MATTERMOST_BASE_URL = os.getenv('MATTERMOST_BASE_URL', 'https://m.ebalina.com/api/v4')

# Mattermost Channel IDs
MATTERMOST_CHANNEL_1 = os.getenv('MATTERMOST_CHANNEL_1', 'x9idtdiwuinu7xminyk9opysuh')
MATTERMOST_CHANNEL_2 = os.getenv('MATTERMOST_CHANNEL_2', 'tmbu97ry3fy8xcrsuzhaz8378c')

# Target Mattermost Channels
TARGET_MATTERMOST_CHANNELS = [MATTERMOST_CHANNEL_1, MATTERMOST_CHANNEL_2] 