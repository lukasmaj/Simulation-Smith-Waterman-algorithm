function test()
    AImageImage = ['X','G','G','T','T','G','A','C','T','A'];
    BImageImage = ['Y','T','G','T','T','A','C','G','G'];
    W1=2 ;
    
    ScoringMatrix = FillScoringMatrix(AImageImage, BImageImage, W1);
    MaxScore = ComputeMaxScore (ScoringMatrix, AImageImage, BImageImage);    
    Find = ComputeAligment(ScoringMatrix, MaxScore);

    for i=1:length(Find)
        a=Find(7-i+1,1,1);
        b=Find(7-i+1,1,2);
        disp([AImageImage(a),' ',BImageImage(b)])
    end
end

function ret = ComputeMaxScore (ScoringMatrix, AImageImage, BImageImage)
    MaxScore=[0,0,0];
    for i = 2:length(AImageImage)
        for j = 2:length(BImageImage)
            if ScoringMatrix(i,j) > MaxScore(1)
               MaxScore=[ScoringMatrix(i,j),i,j]; 
            end
        end
    end
    ret = MaxScore;
end

function ret = FillScoringMatrix(AImageImage, BImageImage, Wk)
    ScoringMatrix=zeros(length(AImageImage),length(BImageImage));
    for i = 2:length(AImageImage)
        for j = 2:length(BImageImage)
            Cross = ScoringCross(ScoringMatrix,i,j,AImageImage,BImageImage);
            Up    = ScoringUp(ScoringMatrix,i,j,Wk);
            Left  = ScoringLeft(ScoringMatrix,i,j,Wk);
            D = 0;
            ScoringMatrix(i,j)= max([Cross,Up,Left,D]);
        end
    end
    ret = ScoringMatrix;
end

function ret = ComputeAligment(ScoringMatrix, MaxScore)
    Find=zeros(100,1,2);
    NextScore = MaxScore; 
    Length= 0;
    while NextScore(1) > 0
        i = NextScore(2);
        j = NextScore(3);

        Find(Length+1,1,1) = i;
        Find(Length+1,1,2) = j;

        NextScore = [ScoringMatrix(i-1,j-1),i-1,j-1];
        if ScoringMatrix(i-1,j) > NextScore(1)
            NextScore = [ScoringMatrix(i-1,j),i-1,j];
        end
        if ScoringMatrix(i,j-1) > NextScore(1)
            NextScore = [ScoringMatrix(i,j-1),i,j-1];
        end
        Length=Length+1;
    end
    ret = Find(1:Length,:,:);
end

function ret = ScoringUp (ScoringMatrix,i,j,Wk)
    ret = ScoringMatrix(i-1,j)-Wk;
end


function ret = ScoringLeft (ScoringMatrix,i,j,Wk)
    ret = ScoringMatrix(i,j-1)-Wk;
end

function ret = ScoringCross (ScoringMatrix,i,j,AImage,BImage)
    ret = ScoringMatrix(i-1,j-1) + Score(AImage(i),BImage(j));
end

function ret = Score(a,b)
    if a==b
        ret = 3;
    else
        ret = -3;
    end
end