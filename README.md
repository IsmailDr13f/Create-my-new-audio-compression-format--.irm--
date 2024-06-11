# Compression Tool with IRM Extension

### 1. Introduction

This project focuses on implementing a lossless compression extension called `.irm`. The primary goal is to manage the compression process and create a graphical interface named `G5-Converter` to compress audio files into the IRM format. This interface also provides features to listen to and evaluate the compression performance.
![image](https://github.com/IsmailDr13f/Create-my-new-audio-compression-format--.irm--/assets/128002689/a0b7b650-74f1-4278-a3f1-f57044bc9749)

### 2. IRM Extension for Lossless Compression

#### 2.1. IRM Header

The IRM file header is crucial for ensuring correct reading and interpretation of the audio information within IRM files. A valid header is necessary for audio playback and processing programs to correctly read or decode IRM files. The header structure is as follows:

| Name            | Size       | Description                                                   |
|-----------------|------------|---------------------------------------------------------------|
| Magic_number    | 3 bytes    | Defines the file format as IRM using the keyword IRM.         |
| Sample_rate     | 4 bytes    | The audio sampling frequency.                                 |
| Bit_depth       | 4 bytes    | Number of bits.                                               |
| Channel_count   | 4 bytes    | Number of channels.                                           |
| Audio_data_size | 4 bytes    | Size of the original audio data.                              |
| Dict_size       | 4 bytes    | Size of the Huffman dictionary.                               |
| Metadata        | 0 < N bytes| Stores useful information about audio compression.            |
| Start_data      | 4 bytes    | Start of the data determined by the keyword 'data'.           |

#### 2.2. Data Normalization

Normalizing audio data is essential for handling different volume levels, positive and negative values, and floating-point numbers above 255. Without normalization, issues like inconsistent volume levels and signal distortion during playback can arise. Normalization ensures consistent and predictable volume levels, facilitating better audio file handling and comparison.

### 3. Components of G5-Converter

The `G5-Converter` interface comprises several components aimed at efficient audio compression and performance evaluation:

- **Encoder**: Compresses audio files using the Huffman coding algorithm.
- **Decoder**: Decompresses IRM files back to their original audio format.
- **Binary File Writing**: Manages the storage of compressed data in a binary file format.
- **Graphical Interface**: Provides user-friendly options to compress, play, and evaluate audio files.

### 4. Limitations and Disadvantages

While the IRM format offers optimal data compression while maintaining quality, there are some limitations and drawbacks that users should be aware of:

- Potential compatibility issues with various audio playback software.
- The need for a valid header to ensure proper decoding and playback.
- Possible challenges in achieving perfect normalization for all types of audio signals.

### 5. Conclusion

This project successfully created a new audio compression format (.IRM) that optimizes data compression without compromising quality. The G5-Converter interface enhances user interaction by providing tools for compression and performance evaluation.
