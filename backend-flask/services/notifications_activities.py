from datetime import datetime, timedelta, timezone

class NotificationsActivities:
    def run():
        now = datetime.now(timezone.utc).astimezone()
        results = [{
            'uuid': '5ceda019-e682-400c-af09-22b05b00ff05',
            'handle':  'Steve Murimi',
            'message': 'Testing the notifications',
            'created_at': (now - timedelta(days=2)).isoformat(),
            'expires_at': (now + timedelta(days=5)).isoformat(),
            'likes_count': 15,
            'replies_count': 3,
            'reposts_count': 2,
            'replies': [{
                'uuid': '9f32a7b2-b507-4300-b7d1-c2134573608b',
                'reply_to_activity_uuid': '5ceda019-e682-400c-af09-22b05b00ff05',
                'handle':  'Worf',
                'message': 'This post has no honor!',
                'likes_count': 0,
                'replies_count': 0,
                'reposts_count': 0,
                'created_at': (now - timedelta(days=2)).isoformat()
            }],
        },
            {
            'uuid': '442699d3-c672-419c-a06b-f5b05478aa02',
            'handle':  'Steve Murimi',
            'message': 'Feedback from a working endpoint',
            'created_at': (now - timedelta(days=7)).isoformat(),
            'expires_at': (now + timedelta(days=9)).isoformat(),
            'likes': 0,
            'replies': []
        },
            {
            'uuid': '81a8360d-133e-4c49-91fd-deb64d81802a',
            'handle':  'Andrew',
            'message': 'Things get tough at first but great in the end',
            'created_at': (now - timedelta(hours=1)).isoformat(),
            'expires_at': (now + timedelta(hours=12)).isoformat(),
            'likes': 0,
            'replies': []
        }
        ]
        return results