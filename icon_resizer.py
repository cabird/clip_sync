#!/usr/bin/env python3
"""
Square Crop and Resize Script
Crops an image to the largest square possible and resizes it to specified dimensions.
"""

import argparse
import os
from PIL import Image
import sys

def crop_to_square(image):
    """
    Crop image to the largest square possible, centered.
    
    Args:
        image: PIL Image object
    
    Returns:
        PIL Image object (square cropped)
    """
    width, height = image.size
    
    # Determine the size of the square (minimum of width and height)
    square_size = min(width, height)
    
    # Calculate coordinates for center crop
    left = (width - square_size) // 2
    top = (height - square_size) // 2
    right = left + square_size
    bottom = top + square_size
    
    # Crop the image
    return image.crop((left, top, right, bottom))

def process_image(input_path, output_size, output_path=None):
    """
    Process an image: crop to square and resize.
    
    Args:
        input_path: Path to input image
        output_size: Desired output size (width and height)
        output_path: Optional output path (if None, auto-generates)
    
    Returns:
        Path to output file
    """
    try:
        # Open the image
        image = Image.open(input_path)
        
        # Convert RGBA to RGB if necessary (for JPEG compatibility)
        if image.mode == 'RGBA':
            # Create a white background
            background = Image.new('RGB', image.size, (255, 255, 255))
            background.paste(image, mask=image.split()[3])  # Use alpha channel as mask
            image = background
        
        # Crop to square
        square_image = crop_to_square(image)
        
        # Resize to desired dimensions
        resized_image = square_image.resize((output_size, output_size), Image.Resampling.LANCZOS)
        
        # Generate output filename if not provided
        if output_path is None:
            base_name = os.path.splitext(os.path.basename(input_path))[0]
            ext = os.path.splitext(input_path)[1]
            # If no extension or unusual extension, default to .png
            if ext.lower() not in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
                ext = '.png'
            output_path = f"{base_name}_{output_size}x{output_size}{ext}"
        
        # Save the image
        if output_path.lower().endswith('.jpg') or output_path.lower().endswith('.jpeg'):
            resized_image.save(output_path, 'JPEG', quality=95)
        else:
            resized_image.save(output_path)
        
        return output_path
        
    except Exception as e:
        print(f"Error processing image: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description='Crop an image to square and resize it to specified dimensions.'
    )
    parser.add_argument(
        'input',
        help='Path to input image'
    )
    parser.add_argument(
        '-d', '--dim',
        type=int,
        required=True,
        help='Output dimensions (e.g., 180 for 180x180)'
    )
    parser.add_argument(
        '-o', '--output',
        help='Output filename (optional, auto-generated if not provided)'
    )
    parser.add_argument(
        '--show-info',
        action='store_true',
        help='Show image information before and after processing'
    )
    
    args = parser.parse_args()
    
    # Validate input file exists
    if not os.path.exists(args.input):
        print(f"Error: Input file '{args.input}' not found.", file=sys.stderr)
        sys.exit(1)
    
    # Validate dimensions
    if args.dim <= 0:
        print(f"Error: Dimensions must be positive. Got: {args.dim}", file=sys.stderr)
        sys.exit(1)
    
    # Show original image info if requested
    if args.show_info:
        try:
            with Image.open(args.input) as img:
                print(f"Original image: {img.size[0]}x{img.size[1]} ({img.mode})")
        except Exception as e:
            print(f"Warning: Could not read image info: {e}", file=sys.stderr)
    
    # Process the image
    output_path = process_image(args.input, args.dim, args.output)
    
    # Show results
    print(f"Successfully created: {output_path}")
    
    if args.show_info:
        try:
            with Image.open(output_path) as img:
                print(f"Output image: {img.size[0]}x{img.size[1]} ({img.mode})")
        except Exception as e:
            print(f"Warning: Could not read output image info: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
