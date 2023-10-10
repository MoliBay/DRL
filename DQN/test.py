import gym

# env = gym.make('CartPole-v0', render_mode="human")

env = gym.make('MountainCar-v0', render_mode="human")

for i_episode in range(20):
    state = env.reset()

    for t in range(1000):
        env.render()
        print(state)
        action = env.action_space.sample()
        state, reward, done, _, _ = env.step(action)

        if done:
            print('Episode #%d finished after %d timesteps' % (i_episode, t))
