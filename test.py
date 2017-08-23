from osim.env.run import RunEnv
env = RunEnv(visualize=False)

observation = env.reset(difficulty = 2)

ball_log = []

pelvis_x = observation[1]
ball_relative = observation[38]
ball_absolute = pelvis_x + ball_relative

ball_log.append(ball_absolute)

for i in range(200):
    observation, reward, done, info = env.step(env.action_space.sample())

    pelvis_x = observation[1]
    ball_relative = observation[38]
    ball_absolute = pelvis_x + ball_relative

    ball_log.append(ball_absolute)

    if done:
        env.reset()
        break

print(ball_log)
