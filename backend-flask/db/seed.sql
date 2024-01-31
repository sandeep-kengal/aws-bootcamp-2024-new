-- this file was manually created
INSERT INTO public.users (display_name, email, handle, cognito_user_id)
VALUES
  ('Andrew Brown','andrew@rocketmail.com' , 'andrewbrown' ,'c4f513be-7bb4-428e-ae87-31926e851fcf'),
  ('AndyBayko','andybayko@rocketmail.com' , 'andybayko' ,'f73f4b05-a59e-468b-8a29-a1c39e7a2222'),
  ('Londo Mollari','lmollari@galaxynet.com' , 'londo' ,'ca5fce02-ce3d-11ed-afa1-0242ac120002'),
  ('joe','murimi101@gmail.com' , 'joe' ,'c8f3905b-0c0d-4f1b-b00d-6ceba95874ed'),
  ('stevecmd','joekadendi@gmail.com' , 'stevecmd' ,'ef6a8993-1b89-435d-990e-b8eeecc118c5');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'stevecmd' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )