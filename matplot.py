import matplotlib.pyplot as plt

x = [2, 4, 5, 6, 3]
y = [4, 16, 25, 36, 9]

#plt.figure(figsize=(6, 4))      # Optional: set figure size
plt.plot(x, y,"r")
plt.xlabel("number")            # Label for x-axis
plt.ylabel("square")            # Label for y-axis
plt.title("line Plot")       # Optional: add a title
#plt.grid(True)                  # Optional: show grid
#plt.tight_layout()              # Helps with label spacing
plt.show()
