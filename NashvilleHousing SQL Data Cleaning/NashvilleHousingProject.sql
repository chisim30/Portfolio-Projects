SELECT *
FROM [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning]

SELECT  COUNT(UniqueID)
FROM [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning]


--Standardize Date Format 

SELECT SaleDate, CONVERT(Date,SaleDate)
FROM [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning]

UPDATE [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning]
SET SaleDate = CONVERT(Date,SaleDate)

-- Populate Property Address

SELECT PropertyAddress
FROM [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning]
WHERE PropertyAddress IS NULL 



SELECT a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress, ISNULL(a.PropertyAddress, b.PropertyAddress)
FROM [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning] a
JOIN [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning]	b
	ON a.ParcelID = b.ParcelID
	AND a.UniqueID != b.UniqueID
WHERE a.PropertyAddress IS Null



UPDATE a
SET PropertyAddress = ISNULL(a.PropertyAddress, b.PropertyAddress)
FROM [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning] a
JOIN [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning]	b
	ON a.ParcelID = b.ParcelID
	AND a.UniqueID != b.UniqueID
WHERE a.PropertyAddress IS Null



--Breaking Address Into Individual Columns (Address,City, State)


SELECT PropertyAddress
FROM [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning] 

SELECT PARSENAME(REPLACE(PropertyAddress, ',', '.'), 2),
PARSENAME(REPLACE(PropertyAddress, ',', '.'), 1)
FROM [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning] 

ALTER TABLE [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning] 
ADD PropertySplitAddress nvarchar(255);

UPDATE [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning] 
SET PropertySplitAddress = PARSENAME(REPLACE(PropertyAddress, ',', '.'), 2)

ALTER TABLE [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning] 
ADD PropertySplitCity nvarchar(255);

UPDATE [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning] 
SET PropertySplitCity = PARSENAME(REPLACE(PropertyAddress, ',', '.'), 1)


-- Splitting the OwnerAddres into separate columns 

SELECT OwnerAddress 
FROM [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning] 

SELECT PARSENAME(REPLACE(OwnerAddress, ',', '.'),3),
PARSENAME(REPLACE(OwnerAddress, ',', '.'),2),
PARSENAME(REPLACE(OwnerAddress, ',', '.'),1)
FROM [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning] 

ALTER TABLE [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning] 
ADD OwnerSplitAddress nvarchar(255);

UPDATE [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning] 
SET OwnerSplitAddress = PARSENAME(REPLACE(OwnerAddress, ',', '.'),3)

ALTER TABLE [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning] 
ADD OwnerSplitCity nvarchar(255);

UPDATE [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning] 
SET OwnerSplitCity = PARSENAME(REPLACE(OwnerAddress, ',', '.'),2)

ALTER TABLE [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning] 
ADD OwnerSplitState nvarchar(255);

UPDATE [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning] 
SET OwnerSplitState = PARSENAME(REPLACE(OwnerAddress, ',', '.'),1)



--Change Y to Yes and N to No 

SELECT  SoldAsVacant, COUNT(SoldAsVacant)
FROM [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning] 
GROUP BY SoldAsVacant


SELECT	SoldAsVacant,
	CASE WHEN SoldAsVacant = 'Y' THEN 'Yes'
	WHEN SoldAsVacant = 'N' THEN 'No'
	ELSE SoldAsVacant 
	END
FROM [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning] 


UPDATE [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning] 
SET SoldAsVacant = CASE WHEN SoldAsVacant = 'Y' THEN 'Yes'
	WHEN SoldAsVacant = 'N' THEN 'No'
	ELSE SoldAsVacant 
	END


--Remove Duplicates 


WITH RowNumCTE AS(
SELECT * ,
	ROW_NUMBER() OVER (
	PARTITION BY ParcelID,
				 PropertyAddress,
				 SalePrice,
				 SaleDate,
				 LegalReference
				 ORDER BY 
					UniqueID
					) AS row_num
FROM [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning] 
)


--DELETE  
--FROM RowNumCTE
--WHERE row_num > 1


SELECT * 
FROM RowNumCTE
WHERE row_num > 1

--Delete Unused Columns

SELECT * 
FROM [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning] 

ALTER TABLE [Portfolio Project].dbo.[Nashville Housing Data for Data Cleaning] 
DROP COLUMN PropertyAddress, TaxDistrict, OwnerAddress



