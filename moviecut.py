from moviepy.editor import *
import os
import cv2

if __name__ == '__main__':
    movies = os.listdir('hoge') #1フォルダの動画を一括取得

    for i in movies:
        movie = movies[i] #編集したい動画のパス

        cap = cv2.VideoCapture("sample.mp4") #動画尺用の動画読み込み
        video_frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT) # フレーム数取得
        video_fps = cap.get(cv2.CAP_PROP_FPS) #フレームレート取得
        video_length = video_frame_count / video_fps #長さ(秒)計算
        
        start = 15 #切り出し開始時刻。秒で表現
        end = video_length - 15 #切り出し終了時刻。後からn秒までと指定
        
        save_path = "./cut/" + movie #編集後のファイル保存先とパス
        
        video = VideoFileClip(file_path).subclip(start, end)
        
        video.write_videofile(save_path,fps=29)


    



