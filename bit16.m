% path = 'new_data';
% imgs = dir('new_data');
path = 'data';
imgs = dir('data');
for i=3:length(imgs)
    fprintf('%.0f\n', i-2);    img = imgs(i).name;
    im = imread([path, '/', img]);
    %imwrite(im, ['bit16_data/', img], 'bitdepth',16);
    im = rgb2gray(im);
    imwrite(im, ['data/', img], 'bitdepth', 16);
end


