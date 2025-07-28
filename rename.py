import os

if True:
    with open("orig_Images.txt", 'r') as f:
        images = f.readlines()

    n_images = int((len(images)-4) / 2)
    for i in range(n_images):
        idx = 2 * i + 4
        image = images[idx]

        img_id = image.split()[0]
        img_name = image.strip().split()[-1]
        img_rest = image.strip().split()[1:-1]

        if int(img_id) <= 638:
            new_img_id = int(img_id) + 373
            new_img_name = f"{int(img_id) - 1 + 373:05d}.png"

        else:
            new_img_id = int(img_id) - 638
            new_img_name = "o"+img_name     # f"{int(img_id) - 1 - 638:05d}.png"

        new_image = " ".join([
            str(new_img_id),
            *img_rest,
            new_img_name,
        ])+"\n"

        images[idx] = new_image

    with open("Images.txt", 'w+') as f:
        f.writelines(images)

if False:
    with open("orig_Points3D.txt", 'r') as f:
        points = f.readlines()

    n_points = len(points) - 3

    for i in range(n_points):
        idx = i + 3
        point = points[idx]
        
        point_rest = point.strip().split()[:8]
        point_tracks = point.strip().split()[8:]

        new_tracks = []
        for t in range(int(len(point_tracks) / 2)):
            old_id = point_tracks[2*t]
            if int(old_id) <= 638:
                new_img_id = int(old_id) + 373
            else:
                new_img_id = int(old_id) - 638

            new_tracks.append(str(new_img_id))
            new_tracks.append(point_tracks[2*t+1])

        new_point = " ".join([
            *point_rest,
            *new_tracks,
        ])+"\n"

        points[idx] = new_point

    with open("Points3D.txt", 'w+') as f:
        f.writelines(points)