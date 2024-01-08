import bpy
import os

def bake_texture(obj, frame_start, frame_step, num_frames, output_folder, image_size):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through the frames
    for i in range(num_frames):
        bpy.context.scene.frame_set(frame_start + i * frame_step)

        # Create a new image for baking
        image_name = f"baked_image_{i+1}"
        new_image = bpy.data.images.new(image_name, width=image_size, height=image_size)

        # Assume the first material of the object has a texture node for baking
        if obj.material_slots:
            mat = obj.material_slots[0].material
            if mat.use_nodes:
                for node in mat.node_tree.nodes:
                    if node.type == 'TEX_IMAGE':
                        node.image = new_image
                        break

        # Baking operation
        bpy.ops.object.bake(type='NORMAL')  # Adjust bake type as needed

        # Save the image
        image_path = os.path.join(output_folder, f"{i + 1}.png")
        new_image.save_render(filepath=image_path)

def main():
    obj = bpy.context.active_object  # Get the selected object
    frame_start = 38 
    frame_step = 3 
    num_frames = 64 
    image_size = 128
    output_folder = "C:\\Users\\Alon\\Desktop\\Rain Sim\\test"  # Set your output folder here

    bake_texture(obj, frame_start, frame_step, num_frames, output_folder, image_size)

if __name__ == "__main__":
    main()
