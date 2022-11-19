import open3d as o3d
import os
pcd = o3d.io.read_point_cloud("points.txt", format='xyz')
print(pcd)
# o3d.visualization.draw_geometries([pcd])